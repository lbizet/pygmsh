# -*- coding: utf-8 -*-
#
import codecs
import os

from setuptools import setup, find_packages

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, 'pygmsh', '__about__.py'), 'rb') as f:
    # pylint: disable=exec-used
    exec(f.read(), about)


def read(fname):
    try:
        content = codecs.open(
            os.path.join(os.path.dirname(__file__), fname),
            encoding='utf-8'
            ).read()
    except FileNotFoundError:
        content = ''
    return content


setup(
    name='pygmsh',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=find_packages(),
    description='Python frontend for Gmsh',
    long_description=read('README.rst'),
    url=about['__website__'],
    download_url='https://pypi.python.org/pypi/pygmsh',
    license=about['__license__'],
    platforms='any',
    install_requires=[
        'meshio',
        'numpy >= 1.9',
        'voropy',
        ],
    extras_require={
        'update': ['pipdate'],
        },
    classifiers=[
        about['__status__'],
        about['__license__'],
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics'
        ]
    )
