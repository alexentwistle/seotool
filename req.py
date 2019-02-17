# 404 Checker
# This checks the http version, sleeps a second, then checks the https version.

import requests
from time import sleep

# Ask user what domain they want to check.

domain = str(input("What domain would you like to check? (Enter the domain part only)\n"))

unsecure_domain = "http://www."+domain
secure_domain = "https://www."+domain
error = "https://www."+domain+"/404/"

# Check response code of the unsecure domain
print(unsecure_domain,':',requests.get(unsecure_domain))

# Sleep a bit
sleep(0.8)

# Check response code of the secure domain
print(secure_domain,':',requests.get(secure_domain))

# Sleep a bit
sleep(0.8)

# Check response code of the error page
print(error,':',requests.get(error))


# This correctly returns the response code when the response code is 200, but:
# TODO - still returns a 200 for a redirect.
# TODO - also, instead of returning 404, it does something weird. 