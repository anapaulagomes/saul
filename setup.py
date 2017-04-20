#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='saul',
    version='0.1.0',
    description='Project Git log analyzer',
    author=['Ana Paula Gomes', 'Marcos Brizeno'],
    author_email=['apgomes88@gmail.com', 'marcos.uece.comp@gmail.com'],
    url='https://github.com/anapaulagomes/saul',
    packages=[
        'saul',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
