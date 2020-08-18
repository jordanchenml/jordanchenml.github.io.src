#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jordan Chen'
SITENAME = 'Powered By Data'
SITEURL = 'https://jordanchenml.github.io'
# https://jordanchenml.github.io

PATH = 'content'
STATIC_PATHS = ['../images', '../theme']

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'

THEME = "/media/jordan/Applications/workspace/projects/jordanchenml.github.io.src/typerite"
# THEME = "/Users/jordanchen/Documents/career/projects/pelican-themes/keep-it-simple"
# THEME = "/Users/jordanchen/Documents/career/projects/pelican-themes/bootlex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Linkedin', 'www.linkedin.com/in/jordan-chenyenting'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

IPYNB_USE_METACELL = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']  
PLUGINS = ['ipynb.markup', 'render_math']
# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints", "._*"]  
