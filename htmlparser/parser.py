# -*- coding: utf-8 -*-

import requests

from html.parser import HTMLParser

from .config import ALLOWED_TEXT_TAGS, TAG_BEGIN_SYMBOLS, TAG_END_SYMBOLS, POSTFIX_ATTR
from .exceptions import URLError
from .utils import write_to_file, prepare_html


class SimpleHTMLParser(HTMLParser):
    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.current_tag = None
        self.print_postfix = None
        self.current_text = ''
        self.write_to_file = write_to_file(self.url)

    def get_page_content(self):
        r = requests.get(self.url)
        if r.status_code != requests.codes.ok:
            raise URLError('Не получен корректный ответ от сервера!')
        return prepare_html(r.text)

    def handle_starttag(self, tag, attrs):
        if tag in ALLOWED_TEXT_TAGS:
            self.current_text += TAG_BEGIN_SYMBOLS.get(tag, '')
            self.current_tag = tag
        else:
            if self.current_tag:
                self.current_text += TAG_BEGIN_SYMBOLS.get(tag, '')
                if tag in POSTFIX_ATTR:
                    attr = POSTFIX_ATTR[tag]
                    attrs = dict(attrs)
                    if attr in attrs:
                        self.print_postfix = attrs[attr]

    def parse(self):
        super().feed(self.get_page_content())

    def handle_endtag(self, tag):
        if tag in ALLOWED_TEXT_TAGS:
            self.current_tag = None
            self.current_text += TAG_END_SYMBOLS.get(tag, '')
            self.write_to_file.send(self.current_text)
            self.current_text = ''
        else:
            self.current_text += TAG_END_SYMBOLS.get(tag, '')

    def handle_data(self, data):
        if self.current_tag:
            self.current_text += data
            if self.print_postfix:
                self.current_text += ' [' + self.print_postfix + ']'
                self.print_postfix = None

    def close(self):
        self.write_to_file.close()
        super().close()

