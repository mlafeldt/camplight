Camplight
=========

Camplight is a simple command-line client for Campfire written in Python.

The Campfire API is documented here: https://github.com/37signals/campfire-api


Usage
-----

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

* Web: <https://github.com/mlafeldt/camplight>
* Mail: <mathias.lafeldt@gmail.com>
* Twitter: [@mlafeldt](https://twitter.com/mlafeldt)


[LICENSE]: https://github.com/mlafeldt/camplight/blob/master/LICENSE
