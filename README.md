About this program:
===================

This is a program written in python that scrapes a URL page for images, specifically for pages that have a "endless scroll" feature such as tumblr.  

To run just type this at the command line:
python endless_scroll_img_scraper.py
and you will be prompted to enter the URL you wish to scrape images from.

Optional command line arugments: 
================================

-- load_time: A float that is how many seconds the program waits for the website to load after each page down while scrolling to the end of the "endless scroll". Default is set to 0.5 seconds. This arg may need to be used to ensure all images are downloaded, dependent on your internet speed, the amount of data per load, etc. This arg can be used to quicken the scraping process, but if the load time is too small it may not scrape all images from the site. Example usage: python endless_scroll_img_scraper.py 0.75 

Requirements
============

* BeautifulSoup
* urllib2
* urllib
* selenium

License
=======


