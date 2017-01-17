from bs4 import BeautifulSoup
import urllib2

"""
domain to crawl http://stroki.net

Page structure sketch:
    homepage has list of poets
    each poet page has poems
    poet URI: http://stroki.net/content/blogcategory/2/3/
        HTML = a.mainlevel
    poem URI: http://stroki.net/content/view/555/3/

"""

# request landing page for site

response = urllib2.urlopen("http://stroki.net")
html = response.read()
decoded = unicode(html, "windows-1251")

soup = BeautifulSoup(decoded, "html.parser")

poet_elements = soup.findAll("a", class_="mainlevel")

for poet_element in poet_elements:
    poet_element = unicode(poet_element)

    # getting the href attribute value manually
    split_element = poet_element.split("href=\"")
    split_link = split_element[1]
    link_list = split_link.split('">')
    link = link_list[0]

    # on to getting the markup for each poet's page
    response = urllib2.urlopen(link)
    html = response.read()
    decoded = unicode(html, "windows-1251")
    soup = BeautifulSoup(decoded, "html.parser")
    poem_elements = soup.findAll("a", class_="mainlevel")
    for poem_element in poem_elements[:3]:
        poem_element = unicode(poem_element)

        # getting the href attribute value manually
        split_element = poem_element.split("\"")
        link = split_element[3]
