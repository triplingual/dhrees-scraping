from bs4 import BeautifulSoup
import urllib2, codecs, os
import re

"""
domain to crawl: http://feb-web.ru/
open dev tools: command option i
create natural link to open Sublime from command line:
ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" ~/bin/subl

Structure of page:

  frames!
  homepage contains []
  each poet page has []

  poet url: http://feb-web.ru/feb/mayakovsky/texts
  poem url: http://feb-web.ru/feb/mayakovsky/texts/ms0/ms1/ms1-033-.htm?cmd=2

  class selector: .
  id selector: #

"""

poem_directory = "feb-web"

if not os.path.exists(poem_directory):
    os.makedirs(poem_directory)


# loop from 001 to 384
for page in range(1, 33):
  try:
    page_number = page.zfill
    response = urllib2.urlopen("http://feb-web.ru/feb/mayakovsky/texts/ms0/ms1/ms1-034-.htm?cmd=2")
  except urllib2.HTTPError, e:
    continue

# try
# catch HTTPError 404 page

# request the landing page for the site
response = urllib2.urlopen("http://feb-web.ru/feb/mayakovsky/texts/ms0/ms1/ms1-034-.htm?cmd=2")

# get the html content using windows 1251 encoding
html = response.read()
decoded = unicode(html, "windows-1251")

# transform the html into a soup object
soup = BeautifulSoup(decoded, 'html.parser')

# find poem title graf
poem = soup.find("p", class_="zag10ot30arr")
poem_title = poem.contents[0].contents[0].string

poem_stanzas = soup.find_all("p", class_=re.compile("stih10ot"))

poem_stanzas[0].find("div", style="display:none;").extract()
poem_date = poem_stanzas[0].find("p", class_="podp-lev").extract().i.string

if len(poem_stanzas[0]) > 0:

# TODO: extract page number SPANs
# TODO: extract line number SPANs
# NOTE: poem named "150 000 000" has formatting that might hork things
  body = poem_stanzas[0].getText()
  author = "mayakovsky"
  date = poem_date

  fp = codecs.open(poem_directory + "/" + author + "--" + poem_title + "--" + date + ".txt", "w", "utf-8")
  fp.write(body)
  fp.close()

# find all author tags
# a_tags = soup.find_all("a", class_="mainlevel")


"""
"""