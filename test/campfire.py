# -*- coding: utf-8 -*-

import unittest
import mock
import camplight


class CampfireTest(unittest.TestCase):

    def setUp(self):
        self.request = mock.Mock()
        self.campfire = camplight.Campfire(self.request)

    def test_account(self):
        expect = {'subdomain': 'foobar', 'id': 12345678}
        self.request.get.return_value = {'account': expect}
        result = self.campfire.account()
        self.request.get.assert_called_once_with('/account')
        self.assertEqual(result, expect)

    def test_rooms(self):
        expect = [{'name': 'Serious'}, {'name': 'Danger'}]
        self.request.get.return_value = {'rooms': expect}
        result = self.campfire.rooms()
        self.request.get.assert_called_once_with('/rooms')
        self.assertEqual(result, expect)

    def test_room_by_name(self):
        rooms = [{'name': 'Serious', 'id': 1000}, {'name': 'Danger', 'id': 2000}]
        self.campfire.rooms = mock.Mock(return_value=rooms)
        result = self.campfire.room('Serious')
        self.assertEqual(result.room_id, 1000)

    def test_room_by_id(self):
        result = self.campfire.room(3000)
        self.assertEqual(result.room_id, 3000)

    def test_room_not_found(self):
        rooms = [{'name': 'Serious', 'id': 1000}]
        self.campfire.rooms = mock.Mock(return_value=rooms)
        self.assertRaises(camplight.RoomNotFoundError, self.campfire.room, 'Danger')

    def test_user_me(self):
        expect = {'name': 'John Doe', 'email_address': 'john.doe@gmail.com'}
        self.request.get.return_value = {'user': expect}
        result = self.campfire.user()
        self.request.get.assert_called_once_with('/users/me')
        self.assertEqual(result, expect)

    def test_user_other(self):
        expect = {'name': 'Alan Turing'}
        self.request.get.return_value = {'user': expect}
        user_id = 6789
        result = self.campfire.user(user_id)
        self.request.get.assert_called_once_with('/users/%s' % user_id)
        self.assertEqual(result, expect)

    def test_presence(self):
        expect = [{'name': 'Danger'}]
        self.request.get.return_value = {'rooms': expect}
        result = self.campfire.presence()
        self.request.get.assert_called_once_with('/presence')
        self.assertEqual(result, expect)

    def test_search(self):
        expect = [{'body': 'ohai', 'type': camplight.MessageType.TEXT}]
        self.request.get.return_value = {'messages': expect}
        result = self.campfire.search('ohai')
        self.request.get.assert_called_once_with('/search/ohai')
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
