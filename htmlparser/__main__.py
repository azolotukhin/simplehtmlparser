# -*- coding: utf-8 -*-

import argparse

from .parser import SimpleHTMLParser


parser = argparse.ArgumentParser()
parser.add_argument('url')
url = parser.parse_args().url
html_parser = SimpleHTMLParser(url)
html_parser.parse()
html_parser.close()
