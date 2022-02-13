# To execute this script
# $pytest staticMethod.py

# Source: https://pypi.org/project/pytest-mock/
# read more: https://pypi.org/project/mock/
# unittest-mock: https://docs.python.org/dev/library/unittest.mock.html
import os

# This is how static method is defined in python
class UnixFS:
    @staticmethod
    def rm(filename):
        os.remove(filename)

def test_unix_fs(mocker):
    # patch:
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')