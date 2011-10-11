#!/usr/bin/env python

"""
Campfire command-line client

Usage: camplight.py <command> [<args>]

The API is described at http://developer.37signals.com/campfire/index
"""

__author__ = 'Mathias Lafeldt <mathias.lafeldt@gmail.com>'
__all__ = ['Campfire', 'Room', 'Sound']

import requests
import simplejson as json


class Request(object):

    def __init__(self, url, token):
        self.url = url
        self._auth = (token, '')

    def _request(self, method, path, data=None):
        headers = None
        if data is not None:
            data = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

        url = self.url + path + '.json'
        r = requests.request(method, url, data=data, headers=headers,
                             auth=self._auth)
        r.raise_for_status()
        # XXX content check too sloppy?
        return json.loads(r.content) if len(r.content) > 1 else None

    def get(self, *args, **kwargs):
        return self._request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._request('POST', *args, **kwargs)

    def put(self, *args, **kwargs):
        return self._request('PUT', *args, **kwargs)


class Campfire(object):

    def __init__(self, request):
        self.request = request

    def rooms(self):
        return self.request.get('/rooms')['rooms']

    def room(self, id):
        try:
            int(id)
        except:
            id = [r['id'] for r in self.rooms() if r['name'] == id][0]
        return Room(self.request, id)

    def user(self, id='me'):
        return self.request.get('/users/%s' % id)['user']

    def presence(self):
        return self.request.get('/presence')['rooms']

    def search(self, term):
        return self.request.get('/search/%s' % term)['messages']


class Room(object):

    def __init__(self, request, room_id):
        self.request = request
        self.room_id = room_id
        self._path = '/room/%s' % self.room_id

    def show(self):
        return self.request.get(self._path)['room']

    def set_name(self, name):
        self.request.put(self._path, data={'room': {'name': name}})

    def set_topic(self, topic):
        self.request.put(self._path, data={'room': {'topic': topic}})

    def recent(self):
        return self.request.get(self._path + '/recent')['messages']

    def transcript(self):
        return self.request.get(self._path + '/transcript')['messages']

    def uploads(self):
        return self.request.get(self._path + '/uploads')['uploads']

    def join(self):
        self.request.post(self._path + '/join')

    def leave(self):
        self.request.post(self._path + '/leave')

    def lock(self):
        self.request.post(self._path + '/lock')

    def unlock(self):
        self.request.post(self._path + '/unlock')

    def speak(self, message, type='TextMessage'):
        data = {'message': {'body': message, 'type': type}}
        return self.request.post(self._path + '/speak', data=data)['message']

    def paste(self, message):
        return self.speak(message, 'PasteMessage')

    def play(self, sound):
        return self.speak(sound, 'SoundMessage')


class Sound(object):
    crickets = 'crickets'
    drama = 'drama'
    greatjob = 'greatjob'
    live = 'live'
    rimshot = 'rimshot'
    tmyk = 'tmyk'
    trombone = 'trombone'
    vuvuzela = 'vuvuzela'
    yeah = 'yeah'


if __name__ == '__main__':
    import sys
    import os

    # TODO add proper option handling
    def handle_cmd(campfire, args):
        cmd = args[1]
        if cmd == 'rooms':
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
                return room.set_name(args[2])
            elif cmd == 'topic':
                return room.set_topic(args[2])
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

    token = os.environ['CAMPFIRE_TOKEN']
    url = os.environ['CAMPFIRE_URL']
    request = Request(url, token)
    campfire = Campfire(request)
    data = handle_cmd(campfire, sys.argv)
    if data:
        # HACK re-encode json for pretty output
        import simplejson as json
        print json.dumps(data, indent=4)
