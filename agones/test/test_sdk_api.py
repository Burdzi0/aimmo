# coding: utf-8

"""
    sdk.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.sdk_api import SDKApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSDKApi(unittest.TestCase):
    """SDKApi unit test stubs"""

    def setUp(self):
        self.api = api.sdk_api.SDKApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_allocate(self):
        """Test case for allocate

        Call to self Allocation the GameServer  # noqa: E501
        """
        pass

    def test_get_game_server(self):
        """Test case for get_game_server

        Retrieve the current GameServer data  # noqa: E501
        """
        pass

    def test_health(self):
        """Test case for health

        Send a Empty every d Duration to declare that this GameSever is healthy  # noqa: E501
        """
        pass

    def test_ready(self):
        """Test case for ready

        Call when the GameServer is ready  # noqa: E501
        """
        pass

    def test_reserve(self):
        """Test case for reserve

        Marks the GameServer as the Reserved state for Duration  # noqa: E501
        """
        pass

    def test_set_annotation(self):
        """Test case for set_annotation

        Apply a Annotation to the backing GameServer metadata  # noqa: E501
        """
        pass

    def test_set_label(self):
        """Test case for set_label

        Apply a Label to the backing GameServer metadata  # noqa: E501
        """
        pass

    def test_shutdown(self):
        """Test case for shutdown

        Call when the GameServer is shutting down  # noqa: E501
        """
        pass

    def test_watch_game_server(self):
        """Test case for watch_game_server

        Send GameServer details whenever the GameServer is updated  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
