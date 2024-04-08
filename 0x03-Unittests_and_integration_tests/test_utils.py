#!/usr/bin/env python3
"""TestAccessNestedMap Module"""

from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """unittest class for access_nested_map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, ex_result):
        """method to test that the method access_nested_ma
        returns what it is supposed to"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, ex_result)


if __name__ == '__main__':
    unittest.main()
