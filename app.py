from bottle import route, run, static_file, template, view
from dt100 import moduleparser

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
    return '<br>'.join(moduleparser())

# Production with GAppEngine
#run(server="gae")

# Development
run(host='localhost', port=9090, debug=True, reloader=True)

