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
    def method(self, *value):
        return 4
            
    #   def test_using_mock():
    #       unittest.mock.mock(Fish)

def test_fish():
    thing = Fish(5, 3)
    thing.method = MagicMock(return_value=3)
    # To assert that a method returns some certain value
    assert 3 == thing.method(3, 4, 5, key='value')
    thing.method.assert_called_with(3, 4, 5, key='value')
    
# To assert that a method has been called with certain parameters

# def foo(m):
#     myobj = m(4)
#     myobj.foo()

# class TestFoo(unittest.TestCase):
#     def test_foo(self):
#         m2 = mock.MagicMock()
#         m = mock.MagicMock(return_value=m2)
#         foo(m)
#         m.assert_called_once_with(4)
#         m2.foo.assert_called_once_with()

# What does this do?
if __name__ == '__main__':
    unittest.main()
