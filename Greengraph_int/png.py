### "geolocation"
### "geolocation"
import geopy
geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

import requests
from url import map_at

### "png"

def is_green(r,g,b):
  threshold=1.1
  return g>r*threshold and g>b*threshold

import png
from itertools import izip

def count_green_in_png(data):
    image=png.Reader(file=StringIO(data.content)).asRGB()
    count = 0
    for row in image[2]:
        pixels=izip(*[iter(row)]*3)
        count+=sum(1 for pixel in pixels if is_green(*pixel))
    return count

from StringIO import StringIO
