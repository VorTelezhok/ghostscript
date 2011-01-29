#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2010 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys

from setuptools import setup, find_packages
import os

long_description="\n\n".join([
    open(os.path.join("README.txt")).read(),
    ])

setup(
    name = "ghostscript",
    version = "0.4",
    install_requires = ['setuptools'],

    packages=find_packages(exclude=['ez_setup']),

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        },

    # metadata for upload to PyPI
    author = "Hartmut Goebel",
    author_email = "h.goebel@crazy-compilers.com",
    description = ("Interface to the Ghostscript C-API, "
                   "both high- and low-level, based on ctypes"),
    long_description = long_description,
    license = "GPL 3.0",
    keywords = "Ghostscript, PDF, Postscript",
    url          = "http://bitbucket.org/htgoebel/python-ghostscript",
    download_url = "http://pypi.python.org/pypi/ghostscript",
    classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    zip_safe = True,
)
