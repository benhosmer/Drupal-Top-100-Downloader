from bottle import route, run, static_file, template, view

import urllib2

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# This allows access to the /static directory and the css files
@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='/Users/bhosmer/Python-Stuff/Drupal-Top-100/appengine-app/static')
    #return static_file(filename, root='/static')

@route('/')
@view('index')
def hello(name='View List'):
    return dict(name=name)

module_list = []
@route('/list-of-modules')
def module_list():
    module_list = []
    count = 0
    module_limit = 100
    soup = BeautifulSoup(urllib2.urlopen('http://drupal.org/project/usage'))
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
    #return '<br>'.join(name)
    return '<br>'.join(module_list)

# Production with GAppEngine
#run(server="gae")

# Development
run(host='localhost', port=9090, debug=True, reloader=True)

