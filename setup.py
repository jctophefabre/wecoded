# -*- coding: utf-8 -*-

__license__ = "MIT"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inrae.fr>"


from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name = 'wecoded',
      version = '0.1',
      description = 'A tool for counting contributed lines by authors on multiple git repositories',
      long_description = readme(),
      author = 'Jean-Christophe Fabre',
      author_email = 'jean-christophe.fabre@inrae.fr',
      url = 'https://github.com/jctophefabre/wecoded',
      license = 'MIT',
      packages = ['wecoded'],
      package_data = {
          'rejocker': ['resources/*']
      },
      entry_points = {
          'console_scripts': [
              'wecoded = wecoded.__main__:main'
          ]
      },
      include_package_data = True,
      install_requires = [
      ],
      python_requires = '~=3.6',
     )