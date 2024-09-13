#!/usr/bin/env python3
""" Unitesting """

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
)


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
