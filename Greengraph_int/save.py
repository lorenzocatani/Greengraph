import geopy
geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

import requests
from url import map_at

import png
from itertools import izip

from StringIO import StringIO

from numpy import linspace

from visualize import show_green_in_png

### "save"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
with open('green.png','w') as green:
    green.write(show_green_in_png(map_at(*london_location,
        zoom=10,satellite=True)))

