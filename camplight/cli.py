# -*- coding: utf-8 -*-

"""
Command-line interface for camplight
"""

import sys
import os

from .api import *


# TODO add proper option handling
def handle_cmd(campfire, args):
    cmd = args[1]
    if cmd == 'account':
        return campfire.account()
    elif cmd == 'rooms':
        return campfire.rooms()
    elif cmd == 'user':
        return campfire.user(args[2])
    elif cmd == 'presence':
        return campfire.presence()
    elif cmd == 'search':
        return campfire.search(args[2])
    else:
        room_id = os.environ['CAMPFIRE_ROOM']
        room = campfire.room(room_id)
        if cmd == 'show':
            return room.show()
        elif cmd == 'name':
            return room.update(name=args[2])
        elif cmd == 'topic':
            return room.update(topic=args[2])
        elif cmd == 'recent':
            return room.recent()
        elif cmd == 'transcript':
            return room.transcript()
        elif cmd == 'uploads':
            return room.uploads()
        elif cmd == 'join':
            return room.join()
        elif cmd == 'leave':
            return room.leave()
        elif cmd == 'lock':
            return room.lock()
        elif cmd == 'unlock':
            return room.unlock()
        elif cmd == 'speak':
            return room.speak(args[2])
        elif cmd == 'paste':
            return room.paste(args[2])
        elif cmd == 'play':
            return room.play(args[2])
        else:
            raise Exception('invalid command')


def main():
    token = os.environ['CAMPFIRE_TOKEN']
    url = os.environ['CAMPFIRE_URL']
    request = Request(url, token)
    campfire = Campfire(request)
    data = handle_cmd(campfire, sys.argv)
    if data:
        # HACK re-encode json for pretty output
        import simplejson as json
        print json.dumps(data, indent=4)
