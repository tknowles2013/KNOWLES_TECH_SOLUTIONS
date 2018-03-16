from requests import get
from bs4 import BeautifulSoup
import csv
import time

with open('challenger2.csv', 'rt') as f:
    data = list(csv.reader(f))

writer = csv.writer(open(r'C:\Users\Rinzler\PycharmProjects\challenge2\challenger2.csv', 'a'))

time.sleep(5)

url = 'https://www.motionpoint.com/'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
print(html_soup.title)

for tags in html_soup.find_all('meta'):
    print(tags.get('content'))

write_title = html_soup.title
# write_link = html_soup('href')
write_meta = html_soup.find_all('meta')

writeArray = [write_title, write_meta]

lenTitle = len(str(write_title))
lenMeta = len(str(write_meta))

lenTotal = lenTitle + lenMeta

printy = sum(len(i) for i in writeArray)

length = len(write_title)
# length1 = len(write_link)
length2 = len(write_meta)
full_length = length + length2

writer.writerow([write_title, write_meta, url, lenTotal])
