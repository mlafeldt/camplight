Camplight
=========

Camplight is a simple command-line client for Campfire written in Python.

The Campfire API is documented here: http://developer.37signals.com/campfire/index


Usage
-----

    $ export CAMPFIRE_URL=https://your-subdomain.campfirenow.com
    $ export CAMPFIRE_TOKEN=your_auth_token

    $ camplight.py rooms
    $ camplight.py presence
    $ camplight.py user me

    $ CAMPFIRE_ROOM=12345 camplight.py recent

    $ CAMPFIRE_ROOM="Develop" camplight.py join
    $ CAMPFIRE_ROOM="Develop" camplight.py speak "You should check out Camplight"


License
-------

See LICENSE file.


Contact
-------

* Web: <https://github.com/mlafeldt/Camplight>
* Mail: <mathias.lafeldt@gmail.com>
