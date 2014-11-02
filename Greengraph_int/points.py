import geopy
geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

import requests
from url import map_at, geolocate
from picturepng import count_green_in_png, is_green

import png
from itertools import izip

from StringIO import StringIO

### "points"

from numpy import linspace
def location_sequence(start,end,steps):
  # Would actually prefer this if steps
  # were deduced from zoomlevel
  # But need projection code for that
  lats=linspace(start[0],end[0],steps)
  longs=linspace(start[1],end[1],steps)
  return zip(lats,longs)

