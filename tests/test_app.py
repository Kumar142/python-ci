import sys
sys.path.append('/Users/kumargaurav/Desktop/python-ci/src')
#from src import app 
from app import index
def test_index():
    assert index() == "Hello, world!"
