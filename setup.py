#!/usr/bin/env python
import os
import re
from setuptools import setup

__doc__="""
Websocket middleware for uwsgi
"""

version = '0.0.1'

setup(name='uwsgi-websockets',
    version=version,
    description=__doc__,
    author='Gavin Wahl',
    author_email='gavinwahl@gmail.com',
    long_description=__doc__,
    packages=['uwsgi_websockets'],
    platforms = "any",
    license='BSD',
    install_requires=['gevent-websocket'],
)
