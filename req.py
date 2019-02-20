# 404 Checker
# This checks the http version, sleeps a second, then checks the https version.

import requests
from time import sleep
from bs4 import BeautifulSoup

# Add User-Agent header
headers = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}


check(url) = requests.get(url,headers = headers)
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



