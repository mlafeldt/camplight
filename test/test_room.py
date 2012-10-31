# -*- coding: utf-8 -*-

import pytest
import mock
import camplight


class TestRoom(object):

    def setup_method(self, method):
        self.request = mock.Mock()
        self.room_id = 27121983
        self.room = camplight.Room(self.request, self.room_id)

    def test_status(self):
        expect = {'name': 'Danger', 'topic': 'No serious discussion'}
        self.request.get.return_value = {'room': expect}
        assert self.room.status() == expect
        self.request.get.assert_called_once_with('/room/%s' % self.room_id)

    def test_recent(self):
        expect = [{'body': 'Hello World', 'type': camplight.MessageType.TEXT}]
        self.request.get.return_value = {'messages': expect}
        assert self.room.recent() == expect
        self.request.get.assert_called_once_with('/room/%s/recent' % self.room_id)

    def test_transcript(self):
        expect = [{'body': 'Hello World', 'type': camplight.MessageType.TEXT}]
        self.request.get.return_value = {'messages': expect}
        assert self.room.transcript() == expect
        self.request.get.assert_called_once_with('/room/%s/transcript' % self.room_id)

    def test_uploads(self):
        expect = [{'name': 'file.png', 'content_type': 'image/png'}]
        self.request.get.return_value = {'uploads': expect}
        assert self.room.uploads() == expect
        self.request.get.assert_called_once_with('/room/%s/uploads' % self.room_id)

    def test_join(self):
        assert self.room.join() == None
        self.request.post.assert_called_once_with('/room/%s/join' % self.room_id)

    def test_leave(self):
        assert self.room.leave() == None
        self.request.post.assert_called_once_with('/room/%s/leave' % self.room_id)

    def test_lock(self):
        assert self.room.lock() == None
        self.request.post.assert_called_once_with('/room/%s/lock' % self.room_id)

    def test_unlock(self):
        assert self.room.unlock() == None
        self.request.post.assert_called_once_with('/room/%s/unlock' % self.room_id)

    def test_speak(self):
        expect = {'body': 'Hello World'}
        self.request.post.return_value = {'message': expect}
        assert self.room.speak('Hello World') == expect
        self.request.post.assert_called_once_with('/room/%s/speak' % self.room_id,
                                                  data={'message': expect})

    def test_paste(self):
        expect = {'body': 'Hello World', 'type': camplight.MessageType.PASTE}
        self.request.post.return_value = {'message': expect}
        assert self.room.paste('Hello World') == expect
        self.request.post.assert_called_once_with('/room/%s/speak' % self.room_id,
                                                  data={'message': expect})

    def test_play(self):
        expect = {'body': camplight.Sound.YEAH, 'type': camplight.MessageType.SOUND}
        self.request.post.return_value = {'message': expect}
        assert self.room.play(camplight.Sound.YEAH) == expect
        self.request.post.assert_called_once_with('/room/%s/speak' % self.room_id,
                                                  data={'message': expect})

    def test_set_name(self):
        assert self.room.set_name('Danger') == None
        self.request.put.assert_called_once_with('/room/%s' % self.room_id,
                                                 data={'room': {'name': 'Danger'}})

    def test_set_topic(self):
        assert self.room.set_topic('No serious discussion') == None
        self.request.put.assert_called_once_with('/room/%s' % self.room_id,
                                                 data={'room': {'topic': 'No serious discussion'}})


if __name__ == '__main__':
    pytest.main(__file__)
