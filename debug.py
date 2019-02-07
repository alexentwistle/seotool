# Simplified version of dual homepage checker purely for playing around and testing. 

import urllib.request
from time import sleep


# Identify one workig URL, and one broken URL.

working  = "http://www.lloydspharmacy.com/en/info/alpecin"

broken = "http://www.lloydspharmacy.com/en/info/alpecin404"

# Check response code of working address
print(working)
print(urllib.request.urlopen(working).getcode())



# Check response code of broken address
# TODO Fix this. It still identifies the broken address as a 404, but in an ugly, broken-looking way.
print(broken)
print(urllib.request.urlopen(broken).getcode())