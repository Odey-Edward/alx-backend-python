#!/usr/bin/env python3
"""client test module"""

from parameterized import parameterized
from client import GithubOrgClient
import unittest
from utils import get_json
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """test class for GithubOrgClient class """

    @parameterized.expand([
        ('google',),
        ('abc',)
        ])
    @patch.object(GithubOrgClient, 'org')
    def test_org(self, param, mock_org):
        """test the org method"""
        mock_org.return_value = None

        obj = GithubOrgClient(param)

        result = obj.org()

        self.assertEqual(result, None)

        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """test for _public_repos_url property"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as puplic_repos_url:

            puplic_repos_url.return_value = {"payload": True}

            obj = GithubOrgClient('google')

            result = obj._public_repos_url

            self.assertEqual(result, {"payload": True})

    @patch('utils.get_json', return_value={"payload": False})
    def test_public_repos(self, mock_json):
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:

            mock_public_repos_url.return_value = {"payload": False}

            obj = GithubOrgClient('abc')

            result = obj._public_repos_url

            self.assertEqual(result, {"payload": False})

            mock_public_repos_url.assert_called_once()

        result = mock_json()

        self.assertEqual(result, {"payload": False})

        mock_json.assert_called_once()
