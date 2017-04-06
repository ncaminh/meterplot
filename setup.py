# -*- coding: utf-8 -*-
#
import codecs
import os
from setuptools import setup, find_packages

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, 'watts', '__about__.py')) as f:
    exec(f.read(), about)


def read(fname):
    try:
        content = codecs.open(
            os.path.join(os.path.dirname(__file__), fname),
            encoding='utf-8'
            ).read()
    except Exception:
        content = ''
    return content


setup(
    name='watts',
    version=about['__version__'],
    packages=find_packages(),
    url='https://github.com/nschloe/watts',
    download_url='https://pypi.python.org/pypi/watts',
    author=about['__author__'],
    author_email=about['__email__'],
    install_requires=[
        'matplotlib',
        'pipdated',
        'pyyaml'
        ],
    description='display energy consumption data',
    long_description=read('README.rst'),
    license=about['__license__'],
    classifiers=[
        about['__status__'],
        about['__license__'],
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Scientific/Engineering :: Visualization'
        ],
    scripts=[
        'tools/watts'
        ]
    )
