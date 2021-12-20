# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def getLinks(url, count, position):
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')[position]
    if (count > 0):
        url = tag.get('href', None)
        getLinks(url, count - 1, position)

url = input('Enter URL:')
if len(url) == 0:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

count = input('Enter count:')
if len(count) == 0:
    count = '4'
count = int(count)

position = input('Enter position:')
if len(position) == 0:
    position = '3'
position = int(position) - 1

getLinks(url, count, position)