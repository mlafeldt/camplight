# -*- coding: utf-8 -*-

import unittest
import random
import mock
import camplight


class RoomTest(unittest.TestCase):

    def setUp(self):
        self.request = mock.Mock()
        self.room_id = random.randint(1, 1000000)
        self.room = camplight.Room(self.request, self.room_id)

    def test_status(self):
        expect = {'name': 'Danger', 'topic': 'No serious discussion'}
        self.request.get.return_value = {'room': expect}
        result = self.room.status()
        self.request.get.assert_called_once_with('/room/%s' % self.room_id)
        self.assertEqual(result, expect)

    def test_recent(self):
        expect = [{'body': 'Hello World', 'type': camplight.MessageType.TEXT}]
        self.request.get.return_value = {'messages': expect}
        result = self.room.recent()
        self.request.get.assert_called_once_with('/room/%s/recent' % self.room_id)
        self.assertEqual(result, expect)

    def test_transcript(self):
        expect = [{'body': 'Hello World', 'type': camplight.MessageType.TEXT}]
        self.request.get.return_value = {'messages': expect}
        result = self.room.transcript()
        self.request.get.assert_called_once_with('/room/%s/transcript' % self.room_id)
        self.assertEqual(result, expect)

    def test_uploads(self):
        expect = [{'name': 'file.png', 'content_type': 'image/png'}]
        self.request.get.return_value = {'uploads': expect}
        result = self.room.uploads()
        self.request.get.assert_called_once_with('/room/%s/uploads' % self.room_id)
        self.assertEqual(result, expect)

    def test_join(self):
        result = self.room.join()
        self.request.post.assert_called_once_with('/room/%s/join' % self.room_id)
        self.assertEqual(result, None)

    def test_leave(self):
        result = self.room.leave()
        self.request.post.assert_called_once_with('/room/%s/leave' % self.room_id)
        self.assertEqual(result, None)

    def test_lock(self):
        result = self.room.lock()
        self.request.post.assert_called_once_with('/room/%s/lock' % self.room_id)
        self.assertEqual(result, None)

    def test_unlock(self):
        result = self.room.unlock()
        self.request.post.assert_called_once_with('/room/%s/unlock' % self.room_id)
        self.assertEqual(result, None)

    def test_speak(self):
        expect = {'body': 'Hello World'}
        self.request.post.return_value = {'message': expect}
        result = self.room.speak('Hello World')
        self.request.post.assert_called_once_with('/room/%s/speak' % self.room_id,
                                                  data={'message': expect})
        self.assertEqual(result, expect)

    def test_paste(self):
        expect = {'body': 'Hello World', 'type': camplight.MessageType.PASTE}
        self.request.post.return_value = {'message': expect}
        result = self.room.paste('Hello World')
        self.request.post.assert_called_once_with('/room/%s/speak' % self.room_id,
                                                  data={'message': expect})
        self.assertEqual(result, expect)

    def test_play(self):
        expect = {'body': camplight.Sound.YEAH, 'type': camplight.MessageType.SOUND}
        self.request.post.return_value = {'message': expect}
        result = self.room.play(camplight.Sound.YEAH)
        self.request.post.assert_called_once_with('/room/%s/speak' % self.room_id,
                                                  data={'message': expect})
        self.assertEqual(result, expect)

    def test_set_name(self):
        result = self.room.set_name('Danger')
        self.request.put.assert_called_once_with('/room/%s' % self.room_id,
                                                 data={'room': {'name': 'Danger'}})
        self.assertEqual(result, None)

    def test_set_topic(self):
        result = self.room.set_topic('No serious discussion')
        self.request.put.assert_called_once_with('/room/%s' % self.room_id,
                                                 data={'room': {'topic': 'No serious discussion'}})
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
