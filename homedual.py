# Basic version of homepage checker. 
# Instead of scraping the page for <a> elements and checking those, this literally just checks the response code of the homepage.
# This checks the http version, sleeps a bit, then checks the https version.


import urllib.request
from time import sleep


# Ask user what domain they want to check.

domain = str(input("What domain would you like to check? Please include www, but not http or https.\n"))

unsecure_domain = "http://"+domain
secure_domain = "https://"+domain



# Check response code of the unsecure domain
print(unsecure_domain)
print(urllib.request.urlopen(unsecure_domain).getcode())

# Sleep a second
sleep(1)

# Check response code of the secure domain
print(secure_domain)
print(urllib.request.urlopen(secure_domain).getcode())

# This correctly returns the response code when the response code is 200, but:
# TODO - still returns a 200 for a redirect.
# TODO - also, instead of returning 404, it does something weird. 