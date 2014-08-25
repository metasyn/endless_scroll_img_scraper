import time
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from urllib import urlretrieve
reload(sys)

if(len(sys.argv) > 1):
	load_time = float(sys.argv[1])
else:
	load_time = 0.5


def imgGreb():
	# get the URL
	print "Enter the URL you wish to scrape.."
	print 'Usage  - "http://uuuu----uuuu.tumblr.com/" <-- With the double quotes'
	myurl = input("@> ")
	# open the URL in the browser
	browser = webdriver.Firefox()
	browser.get(myurl)
	html = browser.page_source
	temp_html = ''
	check_at_end = False
	# scroll to the end of the endless scroll
	while(html != temp_html):
		temp_html = html
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(load_time) # wait for each page to load
		html = browser.page_source
		# double check that we are truly at the end by going through the loop once more
		if(html == temp_html and check_at_end == False):
			temp_html = ''
			check_at_end = True

	soup = BeautifulSoup(html)
	img=soup.findAll(['img'])
	for i in img:
		try:
			# built the complete URL using the domain and relative url you scraped
			url = i.get('src')
			# get the file name 
			name = url.split('/')[-1] 
			# detect if that is a type of pictures you want
			type = name.split('.')[-1]
			if type in ['jpg', 'png']:
				# if so, retrieve the pictures
				urlretrieve(url, name)
		except:
			pass

if __name__ == '__main__':
	imgGreb()