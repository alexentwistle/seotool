# Basic version of homepage checker. 
# Instead of scraping the page for <a> elements and checking those, this literally just checks the response code of the homepage.
# This checks the http version, sleeps a bit, then checks the https version.


import urllib.request
from time import sleep


# Ask user what domain they want to check.

working  = "http://www.lloydspharmacy.com/en/info/alpecin"

broken = "http://www.lloydspharmacy.com/en/info/alpecin404"

# Check response code of working address
print(working)
print(urllib.request.urlopen(working).getcode())

# Check response code of broken address
print(broken)
print(urllib.request.urlopen(broken).getcode())