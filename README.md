Camplight
=========

Camplight is a lightweight Python implementation of the Campfire API.

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
