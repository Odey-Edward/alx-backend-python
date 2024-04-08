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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Implement TestGithubOrgClient.test_public_repos to
        unit-test GithubOrgClient.public_repos"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:

            mock_public_repos_url.return_value = "https://api.example.com/data"

            payload_list = [
                    {'name': 'Edward'},
                    {"name": "repo1"},
                    {"name": "repo2"}]

            mock_json.return_value = payload_list

            obj = GithubOrgClient('abc')

            result = obj.public_repos()

            for v in payload_list:
                self.assertIn(v['name'], result)

            mock_public_repos_url.assert_called_once()

            mock_json.assert_called_once()
