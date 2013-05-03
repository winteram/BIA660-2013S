"""
  BIA 660
  Final Project A sport statistic analysis website

  Author: Han Yan
"""

import cherrypy
import simplejson
from MongoDBHandler import *


###
### Classes
###

class RESTResource(object):
	"""
	Base class for providing a RESTful interface to a resource.

	Support http request:
		handle_GET
		handle_PUT
		handle_POST
		handle_DELETE
	"""
	@cherrypy.expose
	def default(self, *vpath, **params):
		method = getattr(self, "handle_" + cherrypy.request.method, None)
		if not method:
			methods = [x.replace("handle_", "")
			for x in dir(self) if x.startswith("handle_")]
			cherrypy.response.headers["Allow"] = ",".join(methods)
			raise cherrypy.HTTPError(405, "Method not implemented.")
		return method(*vpath, **params);


class BasketballResource(RESTResource):
	"""Class of basketball resoure handler"""

	def __shotChartRequest(self, db, params):
		"""Handler for shot chart query request"""
		year = int(params['year'])
		return db.getShotmap('final_Shot_Map', params['team'], year)

	def __teamStatusRequest(self, db, params):
		"""Handler for team status query request"""
		year = int(params['year'])
		team = params['team']
		attribute = params['attribute']
		order = int(params['order'])
		return db.queryTeamStatus("Regular_Team_Stats", team, attribute, order, year)

	def __finalStatusRequest(self, db, params):
		"""Handler for final status query request"""
		year = params['year']
		team = params['team']
		attr = params['attribute']
		print year, team, attr
		return db.querySF('final_Stats', year, team, attr, '517e7b8d4c59662ed245edbf')


	def __misStatusRequest(self, db, params):
		"""Handler for miscellaneous stats query request"""
		year = int(params['year'])
		team = params['team']
		attribute = params['attribute']
		order = int(params['order'])
		return db.queryTeamStatus("Regular_Mis_Stats", team, attribute, order, year)

	def __topTeamRequest(self, db, params):
		"""Handler for top ten query request"""
		year = int(params['year'])
		attr = params['attribute']
		order = int(params['order'])
		ret = db.getTopTeam('Regular_Team_Stats', attr, year, order)
		for item in ret:
			if item['_id'] == "League Average":
				ret.remove(item)
		return ret
	
	def __finalTotalRequest(self, db, params):
		team = params['team']
		return db.queryFinalAverageTotal('final_Stats', team, '517e7b8d4c59662ed245edbf')

	def __finalEachStatus(self, db, params):
		attr = params['attribute']
		return db.queryFinalEachStatByYear(attr)

	def __finalQuarter(self, db, params):
		attr = params['quarter']
		return db.queryFinalQuarterScore('final_Stats', int(attr), '517e7b8d4c59662ed245edbf')

	def handle_GET(self, *vpath, **params):
		"""Get method handler

		Arguments:
				vpath  -- request url path list.
				params -- request arguments directory.

		Return:

				result of the http get request.

		"""
		cherrypy.response.headers['Origin'] = 'http://api.bia660finalproject.com'
		cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
		requestPath = vpath[0]
		db = NBADBClient('localhost', 27017, 'NBAdata')

		if requestPath == 'shotmap':
			retJson = self.__shotChartRequest(db, params)
		elif requestPath == 'regularstatus':
			retJson = self.__teamStatusRequest(db, params)
		elif requestPath == 'misstatus':
			retJson = self.__misStatusRequest(db, params)
		elif requestPath == 'finalstatus':
			retJson = self.__finalStatusRequest(db, params)
		elif requestPath == 'reqularTopTen':
			retJson = self.__topTeamRequest(db, params)
		elif requestPath == 'finalTotals':
			retJson = self.__finalTotalRequest(db, params)
		elif requestPath == 'finalEachStatus':
			retJson = self.__finalEachStatus(db, params)
		elif requestPath == 'finalQuarter':
			retJson = self.__finalQuarter(db, params)
		

		return simplejson.dumps(retJson)


class FootballResource(RESTResource):
	"""Class of basketball resoure handler"""
	def handle_GET(self, *vpath, **params):
		"""Get method handler

		Arguments:
			vpath  -- request url path list.
			params -- request arguments directory.

		Return:

			result of the http get request.

		"""
		cherrypy.response.headers['Origin'] = 'http://api.bia660finalproject.com'
		cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
		requestPath = vpath[0]
		if requestPath == 'premierleague':
			db = premierLeagueDBClient('localhost', 27017, 'PremierLeaguedata')
			chartName = params['chartName']
			retJson = db.getDataByName('DataCollection', chartName)
			try:
				year = params['year']
			except KeyError:
				try:
					year = params['season']
				except KeyError:
					return simplejson.dumps(retJson)

		return simplejson.dumps(retJson[year])


class RestServer(object):
	"""Class of restfull server that will be published by cherrypy"""
	basketball = BasketballResource()
	football = FootballResource()

	@cherrypy.expose
	def index(self):
		return "This is a rest ful service server."

"""cherrypy server config file"""
conf = {
	'global': {
		'server.socket_host': '0.0.0.0',
		'server.socket_port': 9999,
	}
}

cherrypy.quickstart(RestServer(), '/', conf)
