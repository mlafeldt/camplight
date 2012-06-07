Camplight
=========

Camplight is a simple command-line client for Campfire written in Python.

The Campfire API is documented here: https://github.com/37signals/campfire-api


Usage
-----

    $ export CAMPFIRE_URL=https://your-subdomain.campfirenow.com
    $ export CAMPFIRE_TOKEN=your_auth_token

    $ camplight rooms
    $ camplight presence
    $ camplight user me

    $ CAMPFIRE_ROOM=12345 camplight recent

    $ CAMPFIRE_ROOM="Develop" camplight join
    $ CAMPFIRE_ROOM="Develop" camplight speak "You should check out Camplight"


License
-------

Camplight is licensed under the terms of the MIT License. See [LICENSE] file.


Contact
-------

* Web: <https://github.com/mlafeldt/camplight>
* Mail: <mathias.lafeldt@gmail.com>
* Twitter: [@mlafeldt](https://twitter.com/mlafeldt)


[LICENSE]: https://github.com/mlafeldt/camplight/blob/master/LICENSE
