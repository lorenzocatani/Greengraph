from ..url import geolocate
from nose.tools import assert_equal
from mock import Mock

def test_geolocate():
  """ Test geolocate"""
  # Test something
  #f = Mock(name="myroutine", return_value=2) 
  london_location=geolocate("London")
  expected=(51.5073509, -0.1277583)
  assert_equal(expected,london_location)