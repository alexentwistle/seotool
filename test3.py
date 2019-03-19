import requests
from time import sleep
from bs4 import BeautifulSoup

# Download an HTML document and use the BS library to parse this document.

base = "https://news.sky.com/"
headers = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}

def find_links():
	# Download an HTML document and supply user-agent headers.
	html = requests.get(base, headers=headers)
	# Create an instance of the BeautifulSoup class to parse the HTML document for <a> tags
	soup = BeautifulSoup(html.content,"html.parser")
	links = [a['href'] for a in soup.find_all('a', href=True)]
	records = []
	for url in links:
		print('URL: ', url)
		if url.startswith('#'):
			url = "https://news.sky.com/" + url
			print('FULL URL: ', url)
		elif url.startswith('//'):
			url = "https:" + url
			print('FULL URL: ', url)
		elif url.startswith('/'):
			url = "https://news.sky.com" + url
			print('FULL URL: ', url)

	for url in links:
		status = requests.get(url,headers=headers).status_code
		print(url,": ",status)
	
find_links()


""" TODO This breaks as soon as it encounters a relative URL, so need to add code to turn these into absolute URLs so their response codes are checked
Print them out one per line.
	print("\n".join(link_list))
	for link in link_list:
		status = requests.get(link,headers=headers).status_code
		print(link,":",status)
"""