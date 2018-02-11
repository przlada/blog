#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'Guilherme Toti'
SITENAME = u'Guilherme Toti'
SITEDESCRIPTION = u'technology, programming, studies and random stuff'
SITESUBTITLE = u'technology, programming, studies and random stuff'
SITEURL = ''
COPYRIGHT = 'Guilherme Toti'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'
LOCALE = ['en_US']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Articles and urls
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Social widget
SOCIAL = (
    ('github', 'https://github.com/guilherme-toti'),
    ('facebook', 'http://www.facebook.com/guilhermetoti'),
    ('instagram', 'https://www.instagram.com/guilherme_toti'),
    ('youtube', 'https://www.youtube.com/guilhermetoti'),
)

THEME = 'theme'

MY_CURRENT_AGE = datetime.now().year - 1992

SIDEBAR_DISPLAY = ['categories', 'tags', 'social']

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
ADDTHIS_PUBID = "ra-56c64315810bc72f"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors']
