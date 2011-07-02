Camplight
=========

Camplight is a lightweight Python implementation of the
[Campfire API](http://developer.37signals.com/campfire/index).

In addition to the Python library (camplight.py), the project comes with a
command-line client utilizing it (camplight).


API Usage
---------

    from camplight import Campfire

    cf = Campfire('https://your-subdomain.campfirenow.com', 'your_auth_token')
    print cf.rooms()

    room = cf.room(12345)
    print room.recent()

    room.join()
    room.speak('Campfire rocks!')
    room.play('trombone')
    room.leave()


Client Usage
------------

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

See LICENSE file.


Contact
-------

* Web: <https://github.com/misfire/Camplight>
* Mail: <mathias.lafeldt@gmail.com>
