### "geolocation"
import geopy
geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

import requests
from url import map_at

from picturepng import count_green_in_png, is_green

import png
from itertools import izip

from StringIO import StringIO

### "visualise"

def show_green_in_png(data):
    image=png.Reader(file=StringIO(data.content)).asRGB()
    count = 0
    out=[]
    for row in image[2]:
        outrow=[]
        pixels=izip(*[iter(row)]*3)
        for pixel in pixels:
            outrow.append(0)
            if is_green(*pixel):
                outrow.append(255)
            else:
                outrow.append(0)
            outrow.append(0)
        out.append(outrow)
    buffer=StringIO()
    result = png.from_array(out,mode='RGB')
    result.save(buffer)
    return buffer.getvalue()
