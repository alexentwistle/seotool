# go to homepage
# fetch links (a href) 
# visit links
# - visit link 
# - delay 
# - visit other link ... repeat
# check response code

import urllib.request
from bs4 import BeautifulSoup

domain = "http://www.lloydspharmacy.com/"

# Check response code of the domain
print(domain)
print(urllib.request.urlopen(domain).getcode())

# TODO Crawl domain for links.....

# Specify link URL
url = domain
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,'html.parser')

link_finder = soup.find('a','href')

print(link_finder)