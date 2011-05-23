"""
Campfire API implementation in Python

The API is described at http://developer.37signals.com/campfire/index
"""

__author__ = "Mathias Lafeldt <mathias.lafeldt@gmail.com>"
__data__ = [ 'Campfire', 'CampfireRoom' ]

import urllib2
import simplejson as json

class Campfire(object):
    def __init__(self, url, token):
        self.url = url
        self.token = token
        passwd_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passwd_manager.add_password(None, uri=self.url, user=self.token, passwd='X')
        auth_handler = urllib2.HTTPBasicAuthHandler(passwd_manager)
        self.url_opener = urllib2.build_opener(auth_handler)

    def get(self, path):
        response = self.url_opener.open(self.url + path).read()
        return json.loads(response)

    def put(self, path, data=''):
        request = urllib2.Request(self.url + path, data)
        request.add_header('Content-Type', 'application/json')
        response = self.url_opener.open(request).read().strip()
        return json.loads(response) if len(response) else None

    def rooms(self):
        return self.get('/rooms.json')['rooms']

    def room(self, room_id):
        return CampfireRoom(self, room_id)

    def user(self, user_id):
        return self.get('/users/%s.json' % user_id)['user']

    def me(self):
        return self.get('/users/me.json')['user']

    def presence(self):
        return self.get('/presence.json')['rooms']

    def search(self, term):
        return self.get('/search/%s.json' % term)['messages']


class CampfireRoom(object):
    def __init__(self, campfire, room_id):
        self.campfire = campfire
        self.room_id = room_id

    def get(self, path):
        return self.campfire.get('/room/%s%s' % (self.room_id, path))

    def put(self, path, data=''):
        return self.campfire.put('/room/%s%s' % (self.room_id, path), data)

    def show(self):
        return self.get('.json')['room']

    # FIXME
    def update(self, name='', topic=''):
        data = { 'room': { 'name': name, 'topic': topic } }
        return self.put('/speak.json', json.dumps(data))

    def recent(self):
        return self.get('/recent.json')['messages']

    def transcript(self):
        return self.get('/transcript.json')['messages']

    def uploads(self):
        return self.get('/uploads.json')['uploads']

    def join(self):
        return self.put('/join.json')

    def leave(self):
        return self.put('/leave.json')

    def lock(self):
        return self.put('/lock.json')

    def unlock(self):
        return self.put('/unlock.json')

    def speak(self, message, type='TextMessage'):
        data = { 'message': { 'body': message, 'type': type } }
        return self.put('/speak.json', json.dumps(data))['message']

    def paste(self, message):
        return self.speak(message, 'PasteMessage')

    def play(self, sound):
        return self.speak(sound, 'SoundMessage')
