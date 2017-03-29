from bs4 import BeautifulSoup
import urllib2, codecs, os
import re

text_directory = "legends"

if not os.path.exists(text_directory):
    os.makedirs(text_directory)

# where to go (URL)
url = "http://predanie.ru/rubric-page/iskusstvo-kultura-kritika/?sort=alphabet"
# request URL
response = urllib2.urlopen(url)

# transform response into text object
html = response.read()

# Question: Do we need to change encoding?
# decoded = unicode(html, "windows-1251")

# test variable for content
if len(html) > 0:
    # make Beautiful Soup object
    soup = BeautifulSoup(html, 'html.parser')

    print(soup.find("title"))

    title = soup.find("a", class_="composition__title")

#    print(title)

"""



"""