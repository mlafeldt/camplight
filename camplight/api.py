# -*- coding: utf-8 -*-

"""
Campfire API implementation

The API is described at http://developer.37signals.com/campfire/index
"""

__all__ = ['Request', 'Campfire', 'Room', 'Sound']

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

    def account(self):
        return self.request.get('/account')['account']

    def rooms(self):
        return self.request.get('/rooms')['rooms']

    def room(self, room_id):
        try:
            int(room_id)
        except (TypeError, ValueError, OverflowError):
            room_id = [r['id'] for r in self.rooms()
                       if r['name'] == room_id][0]
        return Room(self.request, room_id)

    def user(self, user_id=None):
        if user_id is None:
            user_id = 'me'
        return self.request.get('/users/%s' % user_id)['user']

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
