from ..url import geolocate
from nose.tools import assert_equal
from mock import Mock

def test_geolocate():
  """ Test is_green"""
  # Test something
  #f = Mock(name="myroutine", return_value=2) 
  b = is_green(5,1,3)
  expected = False
  assert_equal(expected,b)