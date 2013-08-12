History
=======

v0.9.6 (Aug 12 2013)
--------------------

-  Add optional date parameter to ``Room.transcript()``. Format must be
   YYYY/MM/DD. Contributed by @luchux.

v0.9.5 (Jul 16 2013)
--------------------

-  Generate reStructuredText from markdown using
   ``python setup.py doc``. I want to keep using markdown.

v0.9.4 (Jul 16 2013)
--------------------

-  Convert documentation to reStructuredText for PyPI.
-  Recommend using ``pip install camplight`` in README.
-  Define one file per line in MANIFEST.in.

v0.9.3 (Jul 10 2013)
--------------------

-  Add MANIFEST.in for PyPI.

v0.9.2 (Jul 10 2013)
--------------------

-  Fix setup.py for PyPI.

v0.9.1 (Feb 18 2013)
--------------------

-  Use HTTPretty as mock library for unit tests.
-  Add Travis build status to README.
-  Update classifiers in setup.py.

v0.9 (Feb 15 2013)
------------------

-  Fix exit status of ``python setup.py test``.
-  Update copyright year in LICENSE file.

v0.8 (Feb 8 2013)
-----------------

-  Fix JSON decoding in case no text is returned. Reported by @astiam.
-  Travis: run tests against Python 3.3.

v0.7 (Dec 19 2012)
------------------

-  Fix path to Camplight module in unit tests.
-  Update to Requests version 1.0.3.

v0.6 (Nov 6 2012)
-----------------

-  Use `pytest <http://pytest.org>`__ for unit testing.

v0.5 (Oct 30 2012)
------------------

-  Add test coverage using
   `coverage.py <http://nedbatchelder.com/code/coverage/>`__.
   (@keimlink)
-  Properly set ``tests_require`` and ``extras_require`` in setup.py.
   (@keimlink)
-  Work around dependency error returned by ``pip install`` by
   hardcoding the current Camplight version in setup.py. (@jwilder)

v0.4 (Aug 8 2012)
-----------------

-  Add unit tests; run them via ``python setup.py test``.
-  Add Travis CI config.
-  Python 3 compatibility.

v0.3 (Aug 6 2012)
-----------------

-  Rewrite command-line interface from scratch.
-  Add dedicated Camplight exceptions.
-  Make use of ``Response.json`` from Requests v0.12.1.
-  Add verbose mode.
-  More sounds.
-  Tweak per-file docstrings.
-  Add ``setup.py``.
-  Add much more documentation.

v0.2 (Oct 25 2011)
------------------

-  Use `requests <https://github.com/kennethreitz/requests>`__ as HTTP
   library.
-  Move all HTTP/JSON handling to separate class.
-  Split up code into camplight package and runner script.
-  More pythonic coding style. Fix PEP8 errors.
-  Add ability to get account information (account.json).
-  More (undocumented) sounds.
-  Add MIT license text.

v0.1 (May 30 2011)
------------------

-  First tagged version.

