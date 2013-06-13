#!/usr/bin/env python2.7

from distutils.core import setup
from willie import __version__
import tempfile
import os
import shutil

try:
    tmp_dir = tempfile.mkdtemp()
    tmp_main_script = os.path.join(tmp_dir, 'willie')
    shutil.copy('willie.py', tmp_main_script)

    setup(name='willie',
          version=__version__,
          description='Simple and extendible IRC bot',
          author='Edward Powell',
          author_email='powell.518@gmail.com',
          url='http://willie.dftba.net/',
          long_description="""Willie is a simple, lightweight, open source, easy-to-use IRC Utility bot, written in Python. It's designed to be easy to use, easy to run, and easy to make new features for. """,
          packages=['willie', 'willie.modules'],
          scripts=[tmp_main_script],
          license='Eiffel Forum License, version 2',
          platforms='Linux x86, x86-64',
          requires=['MySQLdb', 'feedparser', 'pytz', 'lxml', 'praw', 'enchant', 'tweepy']
         )
finally:
    try:
        shutil.rmtree(tmp_dir)
    except OSError, e:
        if e.errno != 2:  # The directory is already gone, so ignore it
            raise
