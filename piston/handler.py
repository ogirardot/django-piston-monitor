from piston.handler import BaseHandler

class MonitoredBaseHandler(BaseHandler):
	"""
	New BaseHandler to subclass that not only gives you CRUD functionnality for free 
	but also will monitor API calls and triggers signals that will be dealt with saving api calls
	asynchronously.
	 
	"""