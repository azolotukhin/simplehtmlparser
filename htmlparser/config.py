# -*- coding: utf-8 -*-
"""
В этом файле хранятся различные настройки системы

LINE_MAX_LENGTH - максимальная длина строки

ALLOWED_TEXT_TAGS - тэги, из которых будем брать текст
Пример: Брать текст из h1 и p
ALLOWED_TEXT_TAGS = ['h1', 'p']

IGNORE_ATTRS - в тэгах с такими атрибутами мы искать не будем, формат [('название атрибута', 'значение атрибута'), ...]
Пример: не брать текст из любых дочерних элементов тэга с id="menu" и тэга с id="navPath"
IGNORE_ATTRS = [('id', 'menu'), ('id', 'navPath')]

IGNORE_TAGS - в таких тэгах искать не надо
Пример: не брать текст из любых дочерних элементов тэгов aside и header
IGNORE_TAGS = ['aside', 'header']

TAG_BEGIN_SYMBOLS - словарь для выделения нужных тэгов от начала строки
Пример: выделять заголовок h1 как ##
TAG_BEGIN_SYMBOLS = {'h1': '## '}

TAG_END_SYMBOLS - словарь для выделения нужных тэгов с конца строки
Пример: выделять заголовок h1 как ##
TAG_END_SYMBOLS = {'h1': '## '}

POSTFIX_ATTR - Если нужно достать информацию об атрибутах, то можно прописать здесь, будет прописываться в квадратных
скобках после элемента.
В данной задаче используется для ссылок.

"""

LINE_MAX_LENGTH = 80
POSTFIX_ATTR = {'a': 'href'}

# http://lenta.ru/
# http://lenta.ru/news/2016/02/05/sexual_kolne/
ALLOWED_TEXT_TAGS = ['h1', 'h2', 'p']

IGNORE_ATTRS = {}

IGNORE_TAGS = ['nav', 'aside', 'header', 'footer']

TAG_BEGIN_SYMBOLS = {'h1': '>>>> ',
                     'h2': '>>>>>>> '}

TAG_END_SYMBOLS = {'h1': ' <<<<',
                   'h2': ' <<<<<<'}


# http://www.gazeta.ru/
# http://www.gazeta.ru/politics/2016/02/06_a_8060903.shtml
# ALLOWED_TEXT_TAGS = ['h1', 'h2', 'p']
#
# IGNORE_ATTRS = [('class', 'incut'),
#                 ('id', 'article_pants')]
#
# IGNORE_TAGS = ['nav', 'aside', 'header', 'footer']
#
# TAG_BEGIN_SYMBOLS = {'h1': '>>>> ',
#                      'h2': '>>>>>>> ',
#                      'b': '**'}
#
# TAG_END_SYMBOLS = {'h1': ' <<<<',
#                    'h2': ' <<<<<<',
#                    'b': '**'}


# http://aidom.ru/
# http://aidom.ru/hots/2016/start-prodazh-eksklyuzivnih-uchastkov-na-beregu-suhodolskogo-ozera.52.html
# ALLOWED_TEXT_TAGS = ['h1', 'h2', 'p', 'li']
#
# IGNORE_ATTRS = [('id', 'menu'),
#                 ('id', 'navPath')]
#
# IGNORE_TAGS = ['nav', 'aside', 'header', 'footer', 'table']
#
# TAG_BEGIN_SYMBOLS = {'h1': '>>>> ',
#                      'h2': '>>>>>>> ',
#                      'li': ' * '}
#
# TAG_END_SYMBOLS = {'h1': ' <<<<',
#                    'h2': ' <<<<<<'}



# http://www.aif.ru/
# http://www.aif.ru/politics/russia/glava_sevastopolya_ideya_o_dekommunizacii_kryma_-_politicheskaya_shizofreniya
# ALLOWED_TEXT_TAGS = ['h1', 'h2', 'p']
#
# IGNORE_ATTRS = [('class', 'cont_inject')]
#
# IGNORE_TAGS = ['nav', 'aside', 'header', 'footer']
#
# TAG_BEGIN_SYMBOLS = {'h1': '>> ',
#                      'h2': '>>>>> '}
#
# TAG_END_SYMBOLS = {'h1': ' <<',
#                    'h2': ' <<<<'}

