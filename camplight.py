"""
Campfire API implementation in Python

The API is described at http://developer.37signals.com/campfire/index
"""

__author__ = 'Mathias Lafeldt <mathias.lafeldt@gmail.com>'
__all__ = ['Campfire', 'Room', 'Sound']

import urllib
import urllib2
import simplejson as json

def json_encode(obj=None):
    if obj is None:
        obj = {}
    return json.dumps(obj)

def json_decode(s):
    return json.loads(s) if s.startswith('{') else {}

class Campfire(object):
    def __init__(self, url, token):
        self.url = url
        self.token = token
        passwd_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passwd_mgr.add_password(None, uri=self.url, user=self.token, passwd='X')
        auth_handler = urllib2.HTTPBasicAuthHandler(passwd_mgr)
        self.url_opener = urllib2.build_opener(auth_handler)

    def _build_url(self, path):
        return self.url + path + '.json'

    def get(self, path):
        response = self.url_opener.open(self._build_url(path)).read()
        return json_decode(response)

    def post(self, path, data=None):
        request = urllib2.Request(self._build_url(path), json_encode(data))
        request.add_header('Content-Type', 'application/json')
        response = self.url_opener.open(request).read()
        return json_decode(response)

    def put(self, path, data=None):
        request = urllib2.Request(self._build_url(path), json_encode(data))
        request.add_header('Content-Type', 'application/json')
        request.get_method = lambda: 'PUT'
        response = self.url_opener.open(request).read()
        return json_decode(response)

    def rooms(self):
        return self.get('/rooms')['rooms']

    def room(self, id):
        try:
            int(id)
        except:
            id = [r['id'] for r in self.rooms() if r['name'] == id][0]
        return Room(self, id)

    def user(self, id='me'):
        return self.get('/users/%s' % id)['user']

    def presence(self):
        return self.get('/presence')['rooms']

    def search(self, term):
        return self.get('/search/%s' % urllib.quote_plus(term))['messages']


class Room(object):
    def __init__(self, campfire, room_id):
        self.campfire = campfire
        self.room_id = room_id

    def get(self, path=None, **kwargs):
        if path == None:
            path = ''
        return self.campfire.get('/room/%s%s' % (self.room_id, path), **kwargs)

    def post(self, path=None, **kwargs):
        if path == None:
            path = ''
        return self.campfire.post('/room/%s%s' % (self.room_id, path), **kwargs)

    def put(self, path=None, **kwargs):
        if path == None:
            path = ''
        return self.campfire.put('/room/%s%s' % (self.room_id, path), **kwargs)

    def show(self):
        return self.get()['room']

    def set_name(self, name):
        self.put(data={'room': {'name': name}})

    def set_topic(self, topic):
        self.put(data={'room': {'topic': topic}})

    def recent(self):
        return self.get('/recent')['messages']

    def transcript(self):
        return self.get('/transcript')['messages']

    def uploads(self):
        return self.get('/uploads')['uploads']

    def join(self):
        self.post('/join')

    def leave(self):
        self.post('/leave')

    def lock(self):
        self.post('/lock')

    def unlock(self):
        self.post('/unlock')

    def speak(self, message, type='TextMessage'):
        data = {'message': {'body': message, 'type': type}}
        return self.post('/speak', data=data)['message']

    def paste(self, message):
        return self.speak(message, 'PasteMessage')

    def play(self, sound):
        return self.speak(sound, 'SoundMessage')


class Sound(object):
    crickets = 'crickets'
    rimshot = 'rimshot'
    trombone = 'trombone'
