# -*- coding: utf-8 -*-

import pytest
import mock
import camplight


class TestCampfire(object):

    def setup_method(self, method):
        self.request = mock.Mock()
        self.campfire = camplight.Campfire(self.request)

    def test_account(self):
        expect = {'subdomain': 'foobar', 'id': 12345678}
        self.request.get.return_value = {'account': expect}
        assert self.campfire.account() == expect
        self.request.get.assert_called_once_with('/account')

    def test_rooms(self):
        expect = [{'name': 'Serious'}, {'name': 'Danger'}]
        self.request.get.return_value = {'rooms': expect}
        assert self.campfire.rooms() == expect
        self.request.get.assert_called_once_with('/rooms')

    def test_room_by_name(self):
        rooms = [{'name': 'Serious', 'id': 1000}, {'name': 'Danger', 'id': 2000}]
        self.campfire.rooms = mock.Mock(return_value=rooms)
        assert self.campfire.room('Serious').room_id == 1000

    def test_room_by_id(self):
        assert self.campfire.room(3000).room_id == 3000

    def test_room_not_found(self):
        rooms = [{'name': 'Serious', 'id': 1000}]
        self.campfire.rooms = mock.Mock(return_value=rooms)
        with pytest.raises(camplight.RoomNotFoundError):
            self.campfire.room('Danger')

    def test_user_me(self):
        expect = {'name': 'John Doe', 'email_address': 'john.doe@gmail.com'}
        self.request.get.return_value = {'user': expect}
        assert self.campfire.user() == expect
        self.request.get.assert_called_once_with('/users/me')

    def test_user_other(self):
        expect = {'name': 'Alan Turing'}
        self.request.get.return_value = {'user': expect}
        user_id = 6789
        assert self.campfire.user(user_id) == expect
        self.request.get.assert_called_once_with('/users/%s' % user_id)

    def test_presence(self):
        expect = [{'name': 'Danger'}]
        self.request.get.return_value = {'rooms': expect}
        assert self.campfire.presence() == expect
        self.request.get.assert_called_once_with('/presence')

    def test_search(self):
        expect = [{'body': 'ohai', 'type': camplight.MessageType.TEXT}]
        self.request.get.return_value = {'messages': expect}
        assert self.campfire.search('ohai') == expect
        self.request.get.assert_called_once_with('/search/ohai')


if __name__ == '__main__':
    pytest.main(__file__)
