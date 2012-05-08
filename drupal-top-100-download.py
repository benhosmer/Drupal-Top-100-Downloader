
# Include the /bs4 directory so we can import it in case the user doesn't have 
# BeautifulSoup installed already.
import sys
sys.path.append("/bs4")


# We'll need the Regular Expression library to parse our text
import re

# The subprocess library lets us run shell commands:
from subprocess import call

# Beautiful Soup is an HTML parser: http://www.crummy.com/software/BeautifulSoup/bs4/doc/

# This is for an older version of the libray.
# from BeautifulSoup import BeautifulSoup

# This is for Version 4 of BeautifulSoup: pip install beautifulsoup4
from bs4 import BeautifulSoup


# The urllib2 is used to retrieve data from a web page:
import urllib2

# Tell BeautifulSoup the URL to parse:
soup = BeautifulSoup(urllib2.urlopen('http://drupal.org/project/usage'))

# Create our text file and add the necessary canned text to it.
makeFile = open('drupal-100-makefile.make', 'w')
makeFile.write('; This makeFile was generated and downloads the top 100 modules \n')
makeFile.write('; from http://drupal.org/project/usage \n')
makeFile.write('\n')
makeFile.write('core = 6.x \n')
makeFile.write('api = 2 \n')
makeFile.write('\n')
makeFile.close()

printlist = []

# Give the user some feedback so they know the program is doing something.
print "Retrieving module list from drupal.org..."

# Find all the <td> from our URL, then find all the <a> that have an <href>
# Parse out the first 100 items that match our criteria.
# This is very specific to the URL provided earlier
for td in soup.findAll("td"):
    for a in td.findAll("a", {"href": True}):
        printlist.append(a['href'])
for href in printlist:
	moduleList = printlist[1:101]
	

# Now that we have only the first 100 items(it says 101 because drupal core is first), 
# we open our previous text file and add each item after we parse out anything in between the 
# slashes with  a regular expression. We then need to turn this list into a string so we can 
# write each item to the file on a new line.
for items in moduleList:
	makeFile = open('drupal-100-makefile.make', 'a')
	modules = re.sub("/\w+/\w+/", "", items).strip('[],\'')
	makeFile.writelines("projects[] = " + (str(modules) + '\n'))
makeFile.close()
print "Make File, ", makeFile, " created successfully.\n"

# Now that we have a makefile created, we'll use Drush to download all of the modules
# for us.
print "Building site...\n"
call(["drush", "make", "--no-core", "drupal-100-makefile.make", "drupal-modules", "--force-complete", "-y"])
print "Drush make complete.\n"




