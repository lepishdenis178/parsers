import urllib2

from BeautifulSoup import BeautifulSoup



page = urllib2.urlopen('http://yahoo.com').read()

soup = BeautifulSoup(page)

soup.prettify()

for anchor in soup.findAll('a', href=True):

    print anchor['href']
