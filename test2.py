import requests
from time import sleep
from bs4 import BeautifulSoup

# Download an HTML document and use the BS library to parse this document.

url = "https://news.sky.com/story/i-was-gone-former-footballer-glenn-hoddle-died-for-60-seconds-after-tv-studio-cardiac-arrest-11640035"
headers = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}

def find_links():
	# Download an HTML document and supply user-agent headers.
	html = requests.get(url, headers=headers)
	# Create an instance of the BeautifulSoup class to parse the HTML document for <a> tags
	soup = BeautifulSoup(html.content,"html.parser")
	link_list = [a['href'] for a in soup.find_all('a', href=True)]
	link_list.remove('#main')
	link_list.remove('/')
	link_list.remove('/watch-live')

	# Print them out one per line.
	print("\n".join(link_list))
	for link in link_list:
		status = requests.get(link,headers=headers).status_code
		print(link,":",status)
		
find_links()


# TODO This breaks as soon as it encounters a relative URL, so need to add code to turn these into absolute URLs so their response codes are checked
