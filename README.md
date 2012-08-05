Camplight
=========

Camplight is a Python implementation of the [Campfire API].

The project comes with a Python module that can be imported via `import camplight`
and a simple command-line tool named `camplight` to utilize it.


Installation
------------

Camplight requires [Requests] - the excellent HTTP library by Kenneth Reitz.
[This page][Requests-install] explains how to install it.

Camplight itself can be installed via `setup.py`:

    $ git clone git://github.com/mlafeldt/camplight.git
    $ cd camplight/
    $ python setup.py install


API Usage
---------

```python
from camplight import Request, Campfire

request = Request('https://your-subdomain.campfirenow.com', 'your_token')
campfire = Campfire(request)

account = campfire.account()
rooms = campfire.rooms()

room = campfire.room('Danger')
room.join()
room.speak('ohai')
room.leave()
```


Client Usage
------------

    Usage: camplight [options] <command> [args]

    Options:
      -h, --help            show this help message and exit
      -u URL, --url=URL     set Campfire URL
      -t TOKEN, --token=TOKEN
                            set API token for authentication
      -r ROOM, --room=ROOM  set Campfire room
      -v, --verbose         be more verbose

    Global commands:
      account               get account information
      rooms                 list available rooms
      user [id]             get user information
      presence              list rooms the user is present in
      search <term>         search transcripts for term

    Room commands (require --room to be set):
      status                get general room information
      recent                list recent messages in the room
      transcript            list all messages sent today to the room
      uploads               list recently uploaded files in the room
      join                  join the room
      leave                 leave the room
      lock                  lock the room
      unlock                unlock the room
      speak <message>       send a regular chat message
      paste <message>       paste a message
      play <sound>          play a sound
      set-name <name>       change the room's name
      set-topic <topic>     change the room's topic


License
-------

Camplight is licensed under the terms of the MIT License. See [LICENSE] file.


Contact
-------

* Web: <http://mlafeldt.github.com/camplight>
* Mail: <mathias.lafeldt@gmail.com>
* Twitter: [@mlafeldt](https://twitter.com/mlafeldt)


[Campfire API]: https://github.com/37signals/campfire-api
[LICENSE]: https://github.com/mlafeldt/camplight/blob/master/LICENSE
[Requests-install]: http://docs.python-requests.org/en/latest/user/install/
[Requests]: http://python-requests.org
