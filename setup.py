# -*- coding: utf-8 -*-
#
from distutils.core import setup
import os
import codecs

from watts import __version__, __license__, __author__, __email__


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
    version=__version__,
    packages=['watts'],
    url='https://github.com/nschloe/watts',
    download_url='https://pypi.python.org/pypi/watts',
    author=__author__,
    author_email=__email__,
    requires=['matplotlib (>=1.4.0)', 'pyyaml'],
    description='display energy consumption data',
    long_description=read('README.rst'),
    license=__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
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
