import bottle, os, urllib2
from bottle import template, static_file
from datetime import date

app = application = bottle.Bottle()
copyright = date.today().year

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@app.route('/app/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='app')

@app.route('/')
def index():
	return template('index', dict(error = None, year = copyright))


@app.route('/beta')
def index():
	return template('beta', dict(error = None, year = copyright))

@app.route('/donate')
def index():
	return template('donate', dict(error = None, year = copyright))

@app.route('/setup')
def index():
	return template('setup', dict(error = None, year = copyright))

@app.route('/geoCheck')
def index():
        return template('geoCheck.xml', dict(error = None, year = copyright))

@app.route('/status')
def index():
	try:
		data = open('/var/www/portaller/connections.txt','r').readlines()
		try:
			if data[2].strip() != '': 									#loading SNI
				status, text = ('is-visible', 'Open')
			else:
				status, text = ('is-hidden', 'Closed')
		except:
			status, text = ('is-hidden', 'Closed')

		try:
			if data[1].strip() != '': la = data[1].strip() 				#loading LA
			else: ls = 'not available'
		except: ls = 'not available'

		try:
			if data[0].strip() != '': connections = data[0].strip()		#loading connections
			else: connections = 'not available'
		except: connections = 'not available'

	except:
		status, text = ('is-hidden', 'Closed')
		la = connections = 'not available'

	return template('status', dict(error = None, year = copyright, la = la, connections = connections, status = status, text = text))
