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
        assert result == expect

    def test_rooms(self):
        expect = [{'name': 'Serious'}, {'name': 'Danger'}]
        self.request.get.return_value = {'rooms': expect}
        result = self.campfire.rooms()
        self.request.get.assert_called_once_with('/rooms')
        assert result == expect

    def test_user(self):
        expect = {'name': 'John Doe', 'email_address': 'john.doe@gmail.com'}
        self.request.get.return_value = {'user': expect}
        result = self.campfire.user()
        self.request.get.assert_called_once_with('/users/me')
        assert result == expect

    def test_presence(self):
        expect = [{'name': 'Danger'}]
        self.request.get.return_value = {'rooms': expect}
        result = self.campfire.presence()
        self.request.get.assert_called_once_with('/presence')
        assert result == expect

    def test_search(self):
        expect = [{'body': 'ohai', 'type': camplight.MessageType.TEXT}]
        self.request.get.return_value = {'messages': expect}
        result = self.campfire.search('ohai')
        self.request.get.assert_called_once_with('/search/ohai')
        assert result == expect


if __name__ == '__main__':
    unittest.main()
