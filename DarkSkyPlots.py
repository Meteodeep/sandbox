from __future__ import division
import json
import urllib
from os import environ
from sys import exit, argv
import scipy.stats as stats
import matplotlib.pyplot as plt

# The probability and number of standard deviations
# associated with the upper and lower bounds.
pUpper = .95
pLower = .025
nUpper = stats.norm.ppf(pUpper)
nLower = stats.norm.ppf(pLower)

# Get the latitude and longitude from the command line
# or use default values from downtown Naperville.
try:
  lat = argv[1]
  lon = argv[2]
except IndexError:
  lat = 41.772903
  lon = -88.150392

# Get my API key and construct the URL
try:
  with open(environ['HOME'] + '/.darksky') as rcfile:
    for line in rcfile:
      k, v = line.split(':')
      if k.strip() == 'APIkey':
        APIkey = v.strip()
    dsURL = 'https://api.darkskyapp.com/v1/forecast/%s/%s,%s' % (APIkey, lat, lon)
except (IOError, NameError):
  print "Failed to get API key"
  exit()

# Get the data from Dark Sky.
try:
  jsonString = urllib.urlopen(dsURL).read()
  weather = json.loads(jsonString)
except (IOError, ValueError):
  print "Connection failure to %s" % dsURL
  exit()
  
# Pluck out the hourly rain forecast information.
startTime = weather['hourPrecipitation'][0]['time']
intensity = [ x['intensity'] for x in weather['hourPrecipitation'] ]
upper = [ min(x['intensity'] + x['error']/3*nUpper, 75) for x in weather['hourPrecipitation'] ]
lower = [ max(x['intensity'] + x['error']/3*nLower, 0) for x in weather['hourPrecipitation'] ]
time = [ (x['time'] - startTime)/60 for x in weather['hourPrecipitation'] ]

# Plot the intensity ranges.
plt.fill_between([0, 59], [15, 15], [0, 0], color='#0000ff', alpha=.02, linewidth=0)
plt.fill_between([0, 59], [30, 30], [15, 15], color='#0000ff', alpha=.04, linewidth=0)
plt.fill_between([0, 59], [45, 45], [30, 30], color='#0000ff', alpha=.08, linewidth=0)
plt.fill_between([0, 59], [75, 75], [45, 45], color='#0000ff', alpha=.16, linewidth=0)

# Plot the values.
plt.fill_between(time, intensity, color='#ffdd00', linewidth=2)
plt.fill_between(time, upper, intensity, color='#ffdd00', alpha=.25, linewidth=0)
# plt.plot(time, intensity, color='#ff0000', linewidth=3)
# plt.fill_between(time, upper, lower, color='#ff0000', alpha=.25, linewidth=0)
plt.axis([0, 59, 0, 65])
plt.xticks([10, 20, 30, 40, 50])
plt.yticks([7.5, 22.5, 37.5, 55], ['sporadic', 'light', 'moderate', 'heavy'], rotation=90)
plt.tick_params('y', length=0)
plt.xlabel('Minutes from now')
plt.title('Rainfall intensity')

plt.savefig('ds-rain-1.png', dpi=160)
# plt.savefig('ds-rain-2.png', dpi=160)
