
# coding: utf-8

# # Lesson 14

# ## Geoscripting

# Stofzuigerzaag
# 
# Jorn Habes & Maartje Holtslag
# 
# 21-01-2016

#      

# First download the mpl_toolkits basemap from the following url:
# 
#  https://downloads.sourceforge.net/project/matplotlib/matplotlib-toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz

# Install the package typing the following line in the terminal:

# sudo apt-get install basemap

# Now you are ready to start!

# ## Stored Twitter data

# Import the libraries and modules.

# In[34]:

from twython import Twython
import json
from datetime import datetime
from datetime import date
from time import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


# Enter your access codes for Twitter connection.

# In[35]:

APP_KEY =
APP_SECRET =
OAUTH_TOKEN =
OAUTH_TOKEN_SECRET =


# Initiation of the Twython object.

# In[36]:

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


# Determine the search criteria. The entered geocode are the coordinates of Amsterdam. For the best results the count should be set to 100.

# In[61]:

search_results = twitter.search(q='#politie', geocode="52.3740300,4.8896900,50km", count=10)


# Set the name of the output file to the run date and time.

# In[62]:

output_file = 'result_'+datetime.now().strftime('%Y%m%d-%H%M%S')+'.csv' 


# Create the lists for the longitudes and latitudes of the tweets.

# In[63]:

lons = []
lats = []


# Write a function that writes information to a file.

# In[64]:

def write_tweet(t):
    target = open(output_file, 'a')
    target.write(t)
    target.write('\n')
    target.close()


# The following code prints the username of the tweeter and writes the desired information to the previously created file.

# In[65]:

for tweet in search_results["statuses"]:
    username =  tweet['user']['screen_name']
    followers_count =  tweet['user']['followers_count']
    tweettext = tweet['text']
    if tweet['place'] != None:
        full_place_name = tweet['place']['full_name']
        place_type =  tweet['place']['place_type']
        coordinates = tweet['coordinates']
    if coordinates != None:
        latlon = coordinates['coordinates']
        tweet_lon = latlon[0]
        lons += [tweet_lon]
        tweet_lat= latlon[1]
        lats += [tweet_lat]  
    if tweet['created_at'] != None:
        dt = tweet['created_at']
        tweet_datetime = datetime.strptime(dt, '%a %b %d %H:%M:%S +0000 %Y')
    if coordinates != None:
                    string_to_write = str(tweet_datetime)+", "+str(tweet_lat)+", "+str(tweet_lon)+", "+str(tweettext.encode("utf-8"))
                    print string_to_write
                    write_tweet(string_to_write)


# Then create the basemap, showing the Netherlands.

# In[66]:

my_map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=3.363889, llcrnrlat=50.756069,
    urcrnrlon=7.209444, urcrnrlat=53.509299)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'coral')
my_map.drawmapboundary()


# And add the coordinates of the tweets to the map.

# In[67]:

x,y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=4)


# Finally the map can be plotted in a seperate window.

# In[68]:

plt.show()


# This map shows the last 10 tweets about police calls in a radius of 50km around Amsterdam.

# In[ ]:



