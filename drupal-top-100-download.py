#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/bs4")

import urllib2
from subprocess import call

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# Change to another0 value to make it the 'Top n Drupal Modules'
module_limit = 100
filename = 'drupal-{limit}-makefile.make'.format(limit=module_limit)

# Header of the makefile
makefile_preamble = """
; This makeFile was generated and downloads the top 100 modules
; from http://drupal.org/project/usage

core = 6.x
api = 2

"""

# Give the user some feedback so they know the program is doing something.
print "Retrieving module list from drupal.org..."

soup = BeautifulSoup(urllib2.urlopen('http://drupal.org/project/usage'))

count = 0
module_list = []
for td in soup.findAll("td"):
    # If our current count exceeds our limit then we have exactly the right
    # number of modules
    if count > module_limit:
        break

    # If the BeautifuSoup tag has an anchor child element then append it to a
    # list for later use. We don't need to use a find here for the anchors
    # since BeautifulSoup uses a little black magic to make child nodes
    # object attributes
    if td.a:
        # Split the string from at each occurence of the '/' character
        # then use the last item in the list it returns
        mod_name = td.a['href'].split('/')[-1]
        mod_name = "projects[] = {module}".format(module=mod_name)
        module_list.append(mod_name)
        count += 1

# Ignore the first entry since it's always drupal
module_list = module_list[1:]
# Open the filename for writing using a context manager.  This will auto close
# the filename when it leaves scope or an exception is thrown.  It's
# equivalent to a try, except, finally block.  This also opens the file up
# once rather than several times which is usually slow.
with open(filename, 'w') as f:
    f.writelines(makefile_preamble)
    f.writelines('\n'.join(module_list))

print "Make File, {name},  created successfully\n".format(name=filename)

# Now that we have a makefile created, we'll use Drush to download all of the modules
# for us.
print "Building site...\n"
call(["drush", "make", "--no-core", filename, "drupal-modules", "--force-complete", "-y"])
print "Drush make complete.\n"
