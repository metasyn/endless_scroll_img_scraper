import time
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
import getopt
from urllib import urlretrieve
reload(sys)

def imgGreb(load_time, file_types):
	# get the URL
        print "=" * 70
        print "Loadtime: ", load_time 
        print "File Types: ", ' '.join(file_types) 
	print "Enter the URL you wish to scrape.."
	print 'Usage  - "http://uuuu----uuuu.tumblr.com/" <-- With the double quotes'
	myurl = input("@> ")
        print "=" * 70
        # make custom folder
        folder_name = str(myurl[7:])
        os.mkdir(folder_name)
        os.chdir(folder_name)
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
			if type in file_types:
				# if so, retrieve the pictures
				urlretrieve(url, name)
		except:
			pass
        print "Finished Scraping"
        print "=" * 70

def main(argv):
    # define default values
    global load_time 
    load_time = 0.5
    global file_types
    file_types = ["jpg", "png"]

    # here we define what our options are
    # we have an option flag, then an argument
    try:
        opts, args = getopt.getopt(argv, "l:f:", ["load_time", "file_types"])
    except getopt.GetoptError:
        # in case theres a mistake
        usage()
        sys.exit()
    for opt, arg in opts:
        if opt in ("-l", "-load_time"):
            load_time = arg
        elif opt in ("-f", "-file_types"):
            file_types = arg.split()
    
    imgGreb(load_time, file_types)

def usage():
    # This function is called when options aren't specified correctly
    print """\n
    
    Proper Option Usage:

    -f OR -file_types: file type names seperated by a space, surrounded by
    quotes, e.g. "jpg png img" or "png svg gif"

    -l OR -load_time: a number that will set desired load times for the page
    """

if __name__ == '__main__':
    main(sys.argv[1:])
    # we exclude the first argv because its the script name
