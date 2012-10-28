import urllib2

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def moduleparser():
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
    return module_list