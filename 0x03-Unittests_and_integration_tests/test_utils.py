#!/usr/bin/env python3
"""TestAccessNestedMap Module"""

from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, memoize
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """unittest class for access_nested_map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, ex_result):
        """method to test that the access_nested_map
        returns what it is supposed to"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, ex_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test for key error exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """unittest class for get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.get_json')
    def test_get_json(self, test_url, test_payload, get_json):
        """method to test that utils.get_json returns
        the expected result"""

        get_json.return_value = test_payload

        result = get_json(test_url)

        get_json.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """unittest for utils.memoize decorator"""

    def test_memoize(self):
        """memoize test method"""

        class TestClass:
            """test class for testing memoize decorator"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            obj = TestClass()

            result1 = obj.a_property()
            result2 = obj.a_property()

            mock_method.assert_called_once()
            self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()
