#!/Users/xuansong/.bin/miniconda3/envs/testing/bin/python
# Python offical documentation: https://docs.pytest.org/en/6.2.x/getting-started.html

# Here in this script I'm going to: 
# 1. Get myself familiar with writing testcases in python

# write a testcase and execute: pytest testing.py

# 2. Practice using test framework and mocks/stubs

# content of test_sysexit.py
import pytest




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