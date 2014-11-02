from ..picturepng import is_green
from nose.tools import assert_equal

def test_geolocate():
  """ Test is_green"""
  # Test something
  #f = Mock(name="myroutine", return_value=2) 
  b = is_green(5,1,3)
  expected = False
  assert_equal(expected,b)