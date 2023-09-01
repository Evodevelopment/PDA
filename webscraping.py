from bs4 import BeautifulSoup
import urllib.request
from time import sleep
from datetime import datetime

def getGoldPrice():
    url = "http://gold.org"
    req = urllib.request.urlopen(url)
    page = req.read()
    scraping = BeautifulSoup(page)
    price = scraping.findAll("td",attrs={"id":"spotpriceCellAsk"})[0].text
    return price


with open("goldPrice.out","w") as f:
    for x in range(0,10):
        sNow = datetime.now().strftime("%I:%M:%S%p")
        f.write("{0}, {1} \n ".format(sNow, getGoldPrice()))
        sleep(1)

#Beautiful Soup is a Python library for pulling data out of HTML and XML files. It helps you to get the data in fun, condensed way.
# It works with your favorite parser to provide idiomatic 
# ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

