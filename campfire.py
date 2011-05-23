"""
Campfire API implementation in Python

The API is described at http://developer.37signals.com/campfire/index
"""

__author__ = "Mathias Lafeldt <mathias.lafeldt@gmail.com>"
__data__ = [ 'Campfire', 'CampfireRoom' ]

import urllib2

class Campfire(object):
    def __init__(self, url, token):
        self.url = url
        self.token = token
        passwd_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passwd_manager.add_password(None, uri=self.url, user=self.token, passwd='X')
        auth_handler = urllib2.HTTPBasicAuthHandler(passwd_manager)
        self.url_opener = urllib2.build_opener(auth_handler)

    def get(self, path):
        return self.url_opener.open(self.url + path).read()

    def put(self, path, data=''):
        request = urllib2.Request(self.url + path, data)
        request.add_header('Content-Type', 'application/xml')
        return self.url_opener.open(request).read()

    def rooms(self):
        return self.get('/rooms.xml')

    def room(self, room_id):
        return CampfireRoom(self, room_id)

    def user(self, user_id):
        return self.get('/users/%s.xml' % user_id)

    def me(self):
        return self.get('/users/me.xml')

    def presence(self):
        return self.get('/presence.xml')

    def search(self, term):
        return self.get('/search/%s.xml' % term)


class CampfireRoom(object):
    def __init__(self, campfire, room_id):
        self.campfire = campfire
        self.room_id = room_id

    def get(self, path):
        return self.campfire.get('/room/%s%s' % (self.room_id, path))

    def put(self, path, data=''):
        return self.campfire.put('/room/%s%s' % (self.room_id, path), data)

    def show(self):
        return self.get('.xml')

    # FIXME
    def update(self, name='', topic=''):
        return self.put('.xml', '<room><name>%s</name><topic>%s</topic></room>' % (name, topic))

    def recent(self):
        return self.get('/recent.xml')

    def transcript(self):
        return self.get('/transcript.xml')

    def uploads(self):
        return self.get('/uploads.xml')

    def join(self):
        return self.put('/join.xml')

    def leave(self):
        return self.put('/leave.xml')

    def lock(self):
        return self.put('/lock.xml')

    def unlock(self):
        return self.put('/unlock.xml')

    def speak(self, message, type='TextMessage'):
        return self.put('/speak.xml', '<message><body>%s</body><type>%s</type></message>' % (message, type))

    def paste(self, message):
        return self.speak(message, 'PasteMessage')

    def play(self, sound):
        return self.speak(sound, 'SoundMessage')
