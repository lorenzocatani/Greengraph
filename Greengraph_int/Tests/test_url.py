from ..url import geolocate, map_at
from nose.tools import assert_equal


def test_geolocate():
  """ Test geolocate""" 
  london_location=geolocate("London")
  expected=(51.5073509, -0.1277583)
  assert_equal(expected,london_location)

  
def test_url():
  """ Test url"""
  map_response=map_at(51.5072, -0.1275, zoom=10)
  url=map_response.url
  expected="http://maps.googleapis.com/maps/api/staticmap?style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&center=51.5072%2C-0.1275&sensor=false&zoom=10&size=400x400"
  assert_equal(expected,url)