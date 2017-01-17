from bs4 import BeautifulSoup
import urllib2, codecs, os

"""
domain to crawl: http://stroki.net/
open dev tools: command option i
create natural link to open Sublime from command line:
ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" ~/bin/subl

Structure of page:

  homepage contains poets
  each poet page has poems

  poet url: http://stroki.net/content/blogcategory/2/3/
  poem url: http://stroki.net/content/view/555/3/

  class selector: .
  id selector: #

"""

poem_directory = "stroki"

if not os.path.exists(poem_directory):
    os.makedirs(poem_directory)

# request the landing page for the site
response = urllib2.urlopen("http://stroki.net/")

# get the html content using windows 1251 encoding
html = response.read()
decoded = unicode(html, "windows-1251")

# transform the html into a soup object
soup = BeautifulSoup(decoded, 'html.parser')

# find all author tags
a_tags = soup.find_all("a", class_="mainlevel")

# examine each a tag object in turn
for a_tag in a_tags[:3]:

  # convert beautiful soup object to a unicode (string) object
  a_tag = unicode(a_tag)

  # split the a tag string each time we see href="
  split_a_tag = a_tag.split('href="')

  # grab the 2nd member of the list (0-based indexing)
  split_link = split_a_tag[1]

  # split that object on ">
  link_list = split_link.split('">')

  # get the clean link value
  link = link_list[0]

  # fetch the html content for link
  response = urllib2.urlopen(link)

  ###
  # Poet page
  ###

  # read the html content from the connection
  html = response.read()

  # decode the html content
  decoded = unicode(html, "windows-1251")

  # transform the html into a soup object
  soup = BeautifulSoup(decoded, 'html.parser')

  # find all author tags
  a_tags = soup.find_all("a", class_="mainlevel")

  # examine each member of the a_tags list
  for a_tag in a_tags:

    # get the string content of a_tag
    a_tag = unicode(a_tag)

    # split the string each time you see "
    quote_list = a_tag.split('"')

    # get the forth member of the quote list
    link = quote_list[3]

    ###
    # Poem page
    ###

    # fetch the html for the poem page
    response = urllib2.urlopen(link)

    # read the html content from the connection
    html = response.read()

    # decode the html content
    decoded = unicode(html, "windows-1251")

    # transform the html into a soup object
    soup = BeautifulSoup(decoded, 'html.parser')

    # find all table tags with class = contentpaneopen on the poem page
    poem_content = soup.find_all("table", class_="contentpaneopen")

    if len(poem_content) > 0:
      title = poem_content[0].find("td").string
      title = title.replace("/", "-")
      title = title.replace(":", "-").strip().strip(",\".")

      body_author = poem_content[1].find("td")
      body = body_author.get_text()
      author = body_author.find("div").string

#    print link, title, body

      fp = codecs.open(poem_directory + "/" + author + "--" + title + ".txt", "w", "utf-8")
      fp.write(body)
      fp.close()

    """
    # write the poem to the filesystem
    with codecs.open(poem, "w", "utf-8") as out:
      out.write(poem)
    """