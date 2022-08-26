#!/Users/xuansong/.bin/miniconda3/envs/testing/bin/python

# To execute this script
# $pytest staticMethod.py

# Write a testcase using mock
import mock
import unittest
import unittest.mock
from unittest.mock import MagicMock

class Fish():
    def __init__(self, speed, size):
        self.speed = speed
        self.size = size
    def method_returns_4(self, *value):
        return 4

class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        firstValue = "geeks"
        secondValue = "gfg"
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(firstValue, secondValue, message)

    def test_fish_method_returns_4(self):
        thing = Fish(5, 3)
        thing.method_returns_4 = MagicMock(return_value=3)
        # To assert that method_returns_4 returns 3 instead of 4 due to mock
        assert 3 == thing.method_returns_4(3, 4, 5, key='value')

    def test_method_returns_4_is_called(self):
        thing = Fish(5, 3)
        thing.method_returns_4 = MagicMock(return_value=3)
        # To assert that a method has been called with certain parameters
        thing.method_returns_4(5)
        thing.method_returns_4.assert_called_with(5)

if __name__ == '__main__':
    unittest.main()
