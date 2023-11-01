import sys
import os
# Convert the relative path to an absolute path
relative_path = '../src'
absolute_path = os.path.abspath(relative_path)

# Append the absolute path to sys.path
sys.path.append(absolute_path)
from app import index
def test_index():
    #assert absolute_path == "/Users/kumargaurav/Desktop/python-ci/src"
    assert index() == "Hello, world!"
