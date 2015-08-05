__author__ = 'ratcave'

from setuptools import setup, find_packages

setup(name='ProPixx Utilities',
      version='0.6',
      description="Some convenience functions for interacting with VPixx's ProPixx Projector",
      author='Nicholas A. Del Grosso',
      author_email='delgrosso@bio.lmu.de',
      packages=find_packages(),
      install_requires=['pypixxlib'],
)