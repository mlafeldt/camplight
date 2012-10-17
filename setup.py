# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import camplight

install_requires = ['requests>=0.12.1']
tests_require = ['mock']

setup(name='camplight',
      version=camplight.__version__,
      author='Mathias Lafeldt',
      author_email='mathias.lafeldt@gmail.com',
      url='https://github.com/mlafeldt/camplight',
      license='MIT',
      description='Python implementation of the Campfire API',
      long_description=open('README.md').read() + '\n\n' +
                       open('HISTORY.md').read(),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
      packages=find_packages(),
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
      test_suite='test')
