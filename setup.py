# -*- coding: utf-8 -*-

from setuptools import Command, find_packages, setup
import sys

install_requires = ['requests>=1.0.3']
tests_require = ['pytest', 'httpretty>=0.5.9']


class PyTest(Command):
    description = 'Runs the test suite.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        errno = pytest.main('test')
        sys.exit(errno)


class PyPandoc(Command):
    description = 'Generates the documentation in reStructuredText format.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def convert(self, infile, outfile):
        import pypandoc
        with open(outfile, 'w+') as f:
            f.write(pypandoc.convert(infile, 'rst'))

    def run(self):
        self.convert('README.md', 'rst/README.rst')
        self.convert('HISTORY.md', 'rst/HISTORY.rst')


setup(name='camplight',
      version='0.9.6',
      author='Mathias Lafeldt',
      author_email='mathias.lafeldt@gmail.com',
      url='https://github.com/mlafeldt/camplight',
      license='MIT',
      description='Python implementation of the Campfire API',
      long_description=open('rst/README.rst').read() + '\n\n' +
                       open('rst/HISTORY.rst').read(),
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      setup_requires=[],
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      camplight=camplight.cli:main
      """,
      cmdclass={'test': PyTest, 'doc': PyPandoc})
