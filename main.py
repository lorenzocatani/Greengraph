
import Greengraph
import geopy
# from Greengraph import geolocate, map_at, count_green_in_png c'è da metterle così esplicite o basta importare tutto??

#url

london_location=geolocate("London")
print london_location

map_response=map_at(51.5072, -0.1275, zoom=10)
url=map_response.url
print url

#png

print count_green_in_png(map_at(*london_location))


#points

[count_green_in_png(map_at(*location,zoom=10,satellite=True))
            for location in location_sequence(
                geolocate("London"),
                geolocate("Birmingham"),
                10)]
	
	
	
# save
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
with open('green.png','w') as green:
    green.write(show_green_in_png(map_at(*london_location,
        zoom=10,satellite=True)))

				
plt.plot([
    count_green_in_png(
        map_at(*location,zoom=10,satellite=True))
          for location in location_sequence(
              geolocate("London"),
              geolocate("Birmingham"),10)])
plt.savefig('greengraph.png')