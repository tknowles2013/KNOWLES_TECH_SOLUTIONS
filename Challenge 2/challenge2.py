# Taran Knowles
# MotionPoint - Technical Analyst Assessment
# Challenge 2
# KNOWLES_TECH_SOLUTIONS

from requests import get
from bs4 import BeautifulSoup
import csv
import time

# function to scrape the title and meta description, given the url
# outputs title, description, url name, and length of title+description to CSV
def scrape(url):

    # initialize writer to append data to CSV file
    # if viewing CSV in excel, close it out at the time of program run to avoid throwing errors
    writer = csv.writer(open(r'uniqueFileName.csv', 'a'))

    # grab URL
    response = get(url)

    # initialize BeautifulSoup parser with URL
    htmlSoup = BeautifulSoup(response.text, 'html.parser')

    # parse and write the title and description to variables (lists)
    writeTitle = htmlSoup.title.contents
    writeMeta = htmlSoup.findAll(attrs={"name": "description"})

    # convert title and description to string to remove fodder and calculate length
    writeTitle = str(writeTitle)
    writeMeta = str(writeMeta)

    # remove fodder from beginning and end of title and description
    writeTitle = writeTitle[:-2]
    writeMeta = writeMeta[:-23]
    writeTitle = writeTitle[2:]
    writeMeta = writeMeta[16:]

    # print title and description to console
    print(writeTitle)
    print(writeMeta)

    # pull length of title and description
    lenTitle = len(str(writeTitle))
    lenMeta = len(str(writeMeta))

    # find total length of title and description
    lenTotal = lenTitle + lenMeta

    # write data to CSV, underneath headers
    writer.writerow([writeTitle, writeMeta, url, lenTotal])

# Start at index/landing page
linkGet = get('https://www.motionpoint.com/')

# initialize BeautifulSoup parser with URL
links_soup = BeautifulSoup(linkGet.text, 'html.parser')

# create a CSV file to store data
with open('uniqueFileName.csv', 'wb') as csvfile:

    # initialize header to overwrite previous data in CSV file
    header = csv.writer(open(r'uniqueFileName.csv', 'w'))

    # write column headers to CSV, under which scraped data will be stored
    header.writerow(['Title', 'Description', 'URL', 'Length'])

# create list of all hrefs found in index/landing page
linkList = []
for link in links_soup.findAll('a'):
    linkList.append(link.get('href'))

# create new list, that of which will store URLs from linkList that are greater than 28 characters
# this is to remove URLs such as https://www.motionpoint.com and https://es.motionpoint.com
long_links = []
for link in linkList:
    length = len(link)
    if length > 28:
        long_links.append(link)

# assign array items to variables to be passed into functions
mainLink = linkList[0]
secondLink = long_links[0]
thirdLink = long_links[1]
fourthLink = long_links[2]
fifthLink = long_links[3]

# run through scraping functions for each passed url, with a 5 second delay in between
scrape(mainLink)
time.sleep(5)
scrape(secondLink)
time.sleep(5)
scrape(thirdLink)
time.sleep(5)
scrape(fourthLink)
time.sleep(5)
scrape(fifthLink)
