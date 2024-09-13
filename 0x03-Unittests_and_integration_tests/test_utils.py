#!/usr/bin/env python3
""" Unitesting """

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
)
from utils import get_json



class TestAccessNestedMap(unittest.TestCase):
    """ Test access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Mapping[str, Any],
        path: Sequence[str], expected: Any
    ) -> None:
        """ Test access_nested_map is working """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        (dict(), ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping[str, Any],
        path: Sequence[str], expected_msg: str
    ) -> None:
        """ Test access_nested_map with raise """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), expected_msg)


class TestGetJson(unittest.TestCase):
    """ Test the get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('requests.get')
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, bool],
        mock_get: unittest.mock.Mock
    ) -> None:
        """ Test the get_json """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
