import requests
from time import sleep
from bs4 import BeautifulSoup

# Download an HTML document and use the BS library to parse this document.

url = "https://news.sky.com/story/i-was-gone-former-footballer-glenn-hoddle-died-for-60-seconds-after-tv-studio-cardiac-arrest-11640035"
headers = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}

def find_links():
	# Download an HTML document and supply user-agent headers.
	html = requests.get(url, headers=headers)
	# Create an instance of the BeautifulSoup class to parse our document.
	soup = BeautifulSoup(html.content,"html.parser")
	for a in soup.find_all('a', href=True):
		print(a['href'])
	
find_links()