"""
  BIA 660
  Final Project A sport statistic analysis website

  Author: Han Yan
"""
import os
import sys
import json
from NBADataCrawler import *
from pymongo import MongoClient
from bson import BSON
from bson.code import Code
from bson.objectid import ObjectId
from bson import json_util

###
### Globals
###

EXIT_ERROR = 1
EXIT_SUCCESS = 0
GAMELIST = ['Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7']
CHAMPIONS = ['LAL', 'LAL', 'SAS', 'DET', 'SAS', 'MIA', 'SAS', 'BOS', 'LAL', 'LAL', 'DAL', 'MIA']
NOCHAMPIONS = ['PHI', 'NJN', 'NJN', 'LAL', 'DET', 'DAL', 'CLE', 'LAL', 'ORL', 'BOS', 'MIA', 'OKC']
FINALSTATSNAMES = ['FG', 'FGA', 'FG%', '3P','3PA', '3P%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']
YEARLIST = [x for x in range(2001, 2013)]

###
### Classes
###

class MongoDBClient(object):
	"""Classes of mongoDB client"""

	def __init__(self, host, port, dbName):
		"""Construct a mongDB client object

		Arguments:
			host   -- hostname or IP address of the instance to connect to
			port   -- host port 
			dbName -- database's name

		"""
		try:
			self.client = MongoClient(host, port)
			self.db = self.client[dbName]
		except:
			print "Unable to connect to database!"
			sys.exit(EXIT_ERROR)

	def insertToCollection(self, collectionName, data):
		collection = self.db[collectionName]
		if data.__class__ == dict:
			collection.insert(data)
		else:
			for item in data:
				collection.insert(item)

	def findDataFromCollection(self, collectionName, match):
		"""Get data from given collection name.

		Argument:
			collectionName -- the name of collection
		"""
		collection = self.db[collectionName]
		return collection.find(match)


class NBADBClient(MongoDBClient):
	"""Classes of mongoDB client"""

	def getTopTeam(self, collectionName, attribute, year, order):
		"""Use mongoDB mapReduce to extract specific attribute data from collection.

		Arguments:
			collectionName -- the name of collection
			attribute      -- which attribute's data

		TODO: this varies since the structure of each document may different.
		"""
		mapper = Code("""
					  function() { 
						  if (this.year == %i) {
							  emit (this.team, this.stats.%s); 
						  }
					  }
					  """ % (year,attribute)) 

		reducer = Code("""
					  function(key, value) {
						  return {'Team':key, 'Value':value};
					  }
					  """)

		result = self.db[collectionName].map_reduce(mapper, reducer, "topTeam")
		ret = []
		for doc in result.find().sort('value', order):
			ret.append(doc)
		return ret

	def getShotmap(self, collectionName, team, year):
		"""Get each team's shot map in each year's game
		"""
		collection = self.db[collectionName]
		cursor = collection.find({"year":year}, {"team" : 1, "data.%s" % team : 1})
		return cursor[0]['data'][team]

	def querySF(self, collectionName, year, team, attribute, oid):
		"""Query for score and four factor of each final game's team

		Arguments:
			year      -- the year of final game
			team      -- team name
			attribute -- query attribute: 'score' or 'Four Factor'

		Return:
			A list of each team's performance in each game of NBA Final Games
		"""
		resultList = []
		collection = self.db[collectionName]
		for game in GAMELIST:
			objectId = ObjectId(str(oid))
			query = "%s.%s.%s" % (year, game, attribute)
			cursor = collection.find({"_id" : objectId}, {query : 1})
			try:
				each = cursor[0][year][game][attribute]
			except KeyError:
				continue
			for player in each:
				if player[0] == team:
					if attribute == 'score':
						quarters = {}
						quarters['score'] = player[1:5]
						quarters['total'] = player[-1]
						resultList.append(quarters)
					else:
						resultList.append(player)
		return resultList

	def queryFinalBasicStatus(self, collectionName, year, oid):
		"""Get both champion and non-champion's basic statistics from final_Stats collection. 
		
		Arguments:
			collectionName -- collection name
			oid            -- final_Stats collection's object id

		Return:
			A dictionary of both team's statistics.
			{'Not champion': [.., .., ..], 'Champion':[.., .., ..]} 
		"""
		retDict = {}
		collection = self.db[collectionName]
		champions = []
		notChampion = []
		func = lambda x,y : round(x+y,2)
		for game in GAMELIST:
				objectId = ObjectId(str(oid))
				teamName = CHAMPIONS[YEARLIST.index(int(year))]
				query = "%s.%s.%s" % (year, game, teamName)
				cursor = collection.find({"_id" : objectId}, {query : 1})
				for each in cursor:
					try:  
						stats = each[year][game][teamName][-1][2:-1]
						champions.append(stats)
					except KeyError:
						continue
		newChampion = champions[0]
		for stats in champions[1:]:
			newChampion = map(func, newChampion, stats)
		newChampion = [round(x/len(champions),3) for x in newChampion]
		retDict['Champion'] = newChampion

		for game in GAMELIST:
				objectId = ObjectId(str(oid))
				teamName = NOCHAMPIONS[YEARLIST.index(int(year))]
				query = "%s.%s.%s" % (year, game, teamName)
				cursor = collection.find({"_id" : objectId}, {query : 1})
				for each in cursor:
					try:  
						stats = each[year][game][teamName][-1][2:-1]
						notChampion.append(stats)
					except KeyError:
						continue
		newChampion = notChampion[0]
		for stats in notChampion[1:]:
			newChampion = map(func, newChampion, stats)
		newChampion = [round(x/len(notChampion),3) for x in newChampion]
		retDict['Not champion'] = newChampion

		return retDict

	def queryFinalEachStatByYear(self, attribute):
		"""Get final game's stat by attribute names.
		"""
		retDict = {}
		Champion = []
		notChampion = []
		for year in YEARLIST:
			result = self.queryFinalBasicStatus('final_Stats', str(year), '5175f87fd0306c22684d2b0e')
			Champion.append(result['Champion'][FINALSTATSNAMES.index(attribute)])
			notChampion.append(result['Not champion'][FINALSTATSNAMES.index(attribute)])
		retDict['Champion'] = Champion
		retDict['NotChampion'] = notChampion
		return retDict

	def queryFinalAverageTotal(self, collectionName, team, oid):
		"""Get average total score by team name.
		"""
		retDict = {}
		for years in YEARLIST:
			if team == "champion":
				result = self.querySF('final_Stats', str(years), CHAMPIONS[YEARLIST.index(years)], 'score', oid)
			else:
				result = self.querySF('final_Stats', str(years), NOCHAMPIONS[YEARLIST.index(years)], 'score', oid)
			totals = 0
			for each in result:
				totals += each['total']
			average = totals / len(result)
			average = round(average, 2)
			retDict[str(years)] = average
		return retDict

	def queryFinalQuarterScore(self, collectionName, quarter, oid):
		"""Get each year final game's average quarter score.
		"""
		retDict = {}
		for years in YEARLIST:
			result = self.querySF('final_Stats', str(years), CHAMPIONS[YEARLIST.index(years)], 'score', oid)
			totals = 0
			for each in result:
				totals += each['score'][quarter-1]
			average = totals / len(result)
			average = round(average, 2)
			retDict[str(years)] = average
		scoreList = []
		for year in range(2001, 2013):
			scoreList.append(retDict[str(year)])
		scoreDict = {}
		scoreDict['Champion'] = scoreList

		retDict = {}
		for years in YEARLIST:
			result = self.querySF('final_Stats', str(years), NOCHAMPIONS[YEARLIST.index(years)], 'score', oid)
			totals = 0
			for each in result:
				totals += each['score'][quarter-1]
			average = totals / len(result)
			average = round(average, 2)
			retDict[str(years)] = average
		scoreList = []
		for year in range(2001, 2013):
			scoreList.append(retDict[str(year)])
		scoreDict['NotChampion'] = scoreList
		
		return scoreDict 		


	def queryTeamStatus(self, collectionName,team, attribute, order, year=0):
		"""Query each year's team's status, if there is no specific year, query every year's status.
		Return:
			A list of each year's status or a single status for a specific team.
		"""
		returnList = []
		collection = self.db[collectionName]
		stats = "stats.%s" % attribute
		if year == 0:
			cursor = collection.find({"team":team}, {stats: 1, "year" : 1})
		elif team == "all":
			cursor = collection.find({"year":2001}, {"team" : 1})
			newList = []
			for each in cursor:
				if each["team"] == "League Average":
					continue
				newList.append(each["team"])
			return newList
		else:
			cursor = collection.find({"team":team, "year":year}, {stats: 1, "year" : 1})
		for each in cursor.sort("year", order):
			statsDict = {}
			statsDict[attribute] = each['stats'][attribute]
			statsDict['year'] = each['year']
			returnList.append(statsDict)
		return returnList;
			

class premierLeagueDBClient(MongoDBClient, list):
	"""Classes of premierLeague database object, also used for La Liga.
	"""
	def insertData(self, collectionName, dirName):
		fileList = []
		os.chdir(dirName)
		for files in os.listdir("."):
			if files.endswith(".json"):
				fileList.append(files)

		for eachFile in fileList:
			eachChart = {}
			with open(eachFile) as data_file:    
				soccerData = json.load(data_file)
			eachChart['chartName'] = eachFile[:-5]
			eachChart['data'] = soccerData
			self.insertToCollection(collectionName, eachChart)

	def getDataByName(self, collectionName, chartName):
		collection = self.db[collectionName]
		cursor = collection.find({"chartName":chartName}, {"data":1})
		return cursor[0]['data']


if __name__ == '__main__':
	'''Construct a PremierLeagueDB client object'''
	#pl_db = premierLeagueDBClient('localhost', 27017, 'PremierLeaguedata')
	
	'''Insert doata to PremierLeagueDB'''
	#pl_db.insertData('DataCollection', '/home/ubuntu/final/Ligadata')

	#print pl_db.getDataByName('DataCollection', '2002 to 2012 Goals Scored of Top Team')

	'''Construct a mongoDB client object'''

	# db = NBADBClient('localhost', 27017, 'NBAdata')

	# '''Construct a CralerUtils object for use'''
	# crawlUtils = CrawlerUtils()

	# '''Construct a url list from year list'''
	# yearList = crawlUtils.addYear(ROOTLINK[0], YEARLIST)

	# '''Construct a SeasonStat object in order to get data from NBA regular seasons'''
	# seasonStat = SeasonStat(yearList)

	# '''Generate final game page's url dictionary for construct FinalStat object'''
	# finalPageUrlDict = seasonStat.getFinalPageUrlDict(OTHER)

	# '''Construct a FinalStat object in order to get data from NBA final games'''
	# finalStat = FinalStat(finalPageUrlDict)

	# '''Get regular season's Team Stats table's data'''
	# teamStatsDict = seasonStat.getStats(TEAM)

	# '''Get regular season's Miscellaneous Stats table's data '''
	# misStatsDict = seasonStat.getStats(MISCELLANEOUS)

	# '''Construct a list of data from dictionary data'''
	# teamStatsList = crawlUtils.addAttribute(teamStatsDict, ALIST_1)
	# print ('Get OK')
	# db.insertToCollection('Regular_Team_Stats', teamStatsList)
	# print ('Insert OK')

	# '''Construct a list of data from dictionary data'''
	# misStatsList = crawlUtils.addAttribute(misStatsDict, ALIST_2)
	# print ('Get OK')
	# db.insertToCollection('Regular_Mis_Stats', misStatsList)
	# print ('Insert OK')

	# '''Get final game's data '''
	# finalStatDict = finalStat.getStats()
	# print ('Get OK')
	# db.insertToCollection('final_Stats', finalStatDict)
	# print ('Insert OK')

	# '''Get final game's shot map'''
	# finalShopMap = finalStat.getShortCharts()
	# print ('Get OK')
	# db.insertToCollection('final_Shot_Map', finalShopMap)
	# print ('Insert OK')

	#print db.querySF('final_Stats', '2002', 'LAL', 'score', '517e7b8d4c59662ed245edbf')
	#print db.queryFinalBasicStatus('final_Stats', str(2003), '5175f87fd0306c22684d2b0e')
	#print db.queryFinalQuarterScore('final_Stats', 2, '5175f87fd0306c22684d2b0e')
	#print db.queryFinalEachStatByYear('FG')

