#!/Users/xuansong/.bin/miniconda3/envs/testing/bin/python
# Python offical documentation: https://docs.pytest.org/en/6.2.x/getting-started.html

# Here in this script I'm going to: 
# 1. Get myself familiar with writing testcases in python

# write a testcase and execute: pytest testing.py

# 2. Practice using test framework and mocks/stubs

# content of test_sysexit.py
import pytest


# In Python, classe names should start with uppercase
# pytest discovers all tests following its Conventions for Python test discovery, so it finds both test_ prefixed functions. There is no need to 
# subclass anything, but make sure to prefix your class with Test otherwise the class will be skipped. We can simply run the module by passing its 
# filename:

# Something to be aware of when grouping tests inside classes is that each test has a unique instance of the class. Having each test share the same 
# # class instance would be very detrimental(harmful, bad) to test isolation and would promote poor test practices. 

#  -k EXPRESSION         only run tests which match the given substring
                        # test names and their parent classes. Example: -k
                        # 'test_other', while -k 'not test_method' matches those
                        # that don't contain 'test_method' in their names. -k 'not
                        # matches. Additionally keywords are matched to classes
                        # 'extra_keyword_matches' set, as well as functions which
#   -m MARKEXPR           only run tests matching given mark expression.


class TestClass:

    def func(self, x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 5

    def f(self):
        # raise SystemExit(1)
        print("Hello world!")

    # Use the raises helper to assert that some code raises an exception:
    def test_mytest(self):
        with pytest.raises(SystemExit):
            print("An exception has been raised")
            self.f()

    # Write a testcase using pytest-mock