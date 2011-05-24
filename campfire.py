"""
Campfire API implementation in Python

The API is described at http://developer.37signals.com/campfire/index
"""

__author__ = 'Mathias Lafeldt <mathias.lafeldt@gmail.com>'
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

    def get(self, path, decode=True):
        response = self.url_opener.open(self.url + path).read()
        return json.loads(response) if decode else response

    def put(self, path, data='', decode=True):
        request = urllib2.Request(self.url + path, data)
        request.add_header('Content-Type', 'application/json')
        response = self.url_opener.open(request).read()
        return json.loads(response) if decode else response

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

    def get(self, path, **kwargs):
        return self.campfire.get('/room/%s%s' % (self.room_id, path), **kwargs)

    def put(self, path, **kwargs):
        return self.campfire.put('/room/%s%s' % (self.room_id, path), **kwargs)

    def show(self):
        return self.get('.json')['room']

    # FIXME can't get it to work
    def update(self, name='', topic=''):
        data = { 'room': { 'name': name, 'topic': topic } }
        return self.put('/speak.json', data=json.dumps(data))

    def recent(self):
        return self.get('/recent.json')['messages']

    def transcript(self):
        return self.get('/transcript.json')['messages']

    def uploads(self):
        return self.get('/uploads.json')['uploads']

    def join(self):
        self.put('/join.json', decode=False)

    def leave(self):
        self.put('/leave.json', decode=False)

    def lock(self):
        self.put('/lock.json', decode=False)

    def unlock(self):
        self.put('/unlock.json', decode=False)

    def speak(self, message, type='TextMessage'):
        data = { 'message': { 'body': message, 'type': type } }
        return self.put('/speak.json', data=json.dumps(data))['message']

    def paste(self, message):
        return self.speak(message, 'PasteMessage')

    def play(self, sound):
        return self.speak(sound, 'SoundMessage')
