# -*- coding: utf-8 -*-

import functools
import os
import textwrap
import uuid

from urllib.parse import urlparse

from bs4 import BeautifulSoup

from .config import LINE_MAX_LENGTH, IGNORE_ATTRS, IGNORE_TAGS


def coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)
        return gen
    return inner


def url_to_filepath(url):
    """
    URL может заканчиваться на слэш, а может заканчиваться на что-то типа .html, .php и т.д.,
    а может ни на то, ни на то.
    Если не можем дать название из урла, то даем просто какое-то уникальное и кладем в дирректорию
    с названием сайта.

    """
    o = urlparse(url)

    file_path = '%s.txt' % uuid.uuid4()
    o_path = o.path.strip('/')
    if o_path:
        split_url_path = o_path.split('/')
        if split_url_path[-1].find('.') != -1:
            url_chank = split_url_path[-1].split('.')
            url_chank[-1] = 'txt'
            split_url_path[-1] = '.'.join(url_chank)
        else:
            split_url_path[-1] += '.txt'
        file_path = '/'.join(split_url_path)
    return os.path.join(os.getcwd(), o.netloc, file_path)


@coroutine
def write_to_file(url):
    filename = url_to_filepath(url)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        while True:
            text = yield
            f.write(textwrap.fill(text, width=LINE_MAX_LENGTH))
            f.write('\n\n')


def prepare_html(html):
    """
    "Готовит" html к последующему парсингу, вырезая ненужные тэги и тэги с ненужными атрибутами.

    """
    soup = BeautifulSoup(html, "html.parser")
    if IGNORE_TAGS:
        tags = soup.findAll(IGNORE_TAGS)
        [tag.extract() for tag in tags]
    for tag_attr_name, tag_attr_value in IGNORE_ATTRS:
        tags = soup.findAll(attrs={tag_attr_name: tag_attr_value})
        [tag.extract() for tag in tags]
    return str(soup)
