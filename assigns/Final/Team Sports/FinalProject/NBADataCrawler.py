"""
	BIA 660
	Final Project: A sport statistic analysis website

	Author: Han Yan
"""


import urllib2
import simplejson
import json
import unicodedata
from BeautifulSoup import BeautifulSoup
import re
from collections import Counter

###
### Globals
###

ROOTLINK = ["http://www.basketball-reference.com/leagues", "http://www.basketball-reference.com/teams"]
YEARLIST = [x for x in range(2013, 2014)]
TEAM = 0
MISCELLANEOUS = 1
OTHER = 2

"""Each team's statistics attribute"""
ALIST_1 = ['G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PTS/G']
ALIST_2 = ['Age', 'PW', 'PL', 'MOV', 'SOS', 'SRS', 'ORtg', 'DRtg', 'Pace', 'O_eFG%', 'O_TOV%', 'O_ORB%', 'O_FT/FGA', 'D_eFG%', 'D_TOV%', 'D_DRB%', 'D_FT/FGA', 'Arena', 'Attendace']


###
### Classes
###

class CrawlerUtils(object):
	"""Class of utils for crawling nba game statistics"""

	def addYear(self, url, yearList):
		"""Add year to the root link

		Arguments:
			url      -- page's url requires add extend year string.
			yearList -- generate year string from this list.

		Returns
			the new url list which has been added extend string to each item.

		"""
		newUrlList = []
		for year in yearList:
			newUrlList.append(url + "/NBA_" + str(year) + ".html")
		return newUrlList

	def addAttribute(self, dataDict, attriList):
		"""Add attribute and adjust each Team's data structure.
		   i.e. {'year': ***, 'team', ***, 'stat': {**, **, **} }

		Arguments:

			dataDict  -- data source.
			attriList -- attribute list.

		Return:

			formed data used to be insert to database.
		"""
		formedList = []
		teamsData = dataDict['data']
		for year in YEARLIST:
			eachYearData = teamsData[year]
			for item in eachYearData.keys():
				formedDict = {}
				formedDict['year'] = year
				formedDict['team'] = item
				stats = {}
				for data in eachYearData[item]:
					stats[attriList[eachYearData[item].index(data)]] = data
				formedDict['stats'] = stats
				formedList.append(formedDict)
		return formedList


class SeasonStat(list):
	"""Class of season statistics"""

	def __init__(self, *yearList):
		"""Construct a SeasonStat object from a year url list"""
		list.__init__(self, *yearList)

	def printList(self):
		"""Just for test"""
		print self

	def __getTable(self, url, flag, pos1, pos2):
		"""Get Team Stats table or Miscellaneous Stats table.

		Arguments:
			url  -- Page's url.
			flag -- flag for extract which table, 0 for Team Stats table, 1 for Miscellaneous Stats table.
			pos1 -- position of Team Stats table
			pos2 -- position of Miscellaneous Stats table

			if flag is not 0 or 1, return required table's position.

		Return:
			Required table section from that page which is a BeautifulSoup object.
		"""
		connect = urllib2.urlopen(url)
		page = connect.read()
		soup = BeautifulSoup(page)
		tables = soup.findAll("table")
		connect.close()
		if flag == TEAM: return tables[pos1]
		elif flag == MISCELLANEOUS: return tables[pos2]
		else: return tables[pos1]

	def __getAttributeList(self, soupTable):
		"""Get the attribute name of each row.

		Argument:

			soupTable -- data table.

		Return:

			A list of attribute name.
		"""
		alist = []
		tr = soupTable.find("thead").find("tr")
		ths = tr.findAll('th')
		for items in ths[2:]:
			alist.append(str(items.text))
		return alist

	def __getContentDict(self, soupTable):
		"""Get the contents from table.

		Argument:

			soupTable -- data table.

		Return:

			A dict with the key of row
		"""
		cDict = {}
		trs = soupTable.find("tbody").findAll("tr")
		for tr in trs:
			cList = []
			tds = tr.findAll("td")
			for td in tds[2:]:
				try:
					cList.append(float(td.text))
				except ValueError:
					cList.append(str(td.text))
			cDict[str(tds[1].text)] = cList
		return cDict

	def getTablesAttrList(self, posOfTable):
		yearUrl = self[0]
		print yearUrl
		table = self.__getTable(yearUrl, 0, posOfTable, 0)
		return self.__getAttributeList(table)

	def getStats(self, flag):
		"""Get data from table

		Argument:

			flag -- flag for return data: 0 for Team Stats, 1 for Miscellaneous Stats.

		Returns:

			A python dictionary including ordered statistics.
		"""
		dataDict = {}
		contentDict = {}
		for year in self:
			table = self.__getTable(year, flag, 12, 14)
			cDict = self.__getContentDict(table)
			contentDict[YEARLIST[self.index(year)]] = cDict
		if flag:
			dataDict["type"] = "Miscellaneous Stats"
		else:
			dataDict["type"] = "Team Stats"
		dataDict["data"] = contentDict
		return dataDict

	def getFinalPageUrlDict(self, flag):
		"""Get each game's page from Final Game table

		Return:

			A python dictionary including each game's page url.
		"""
		contentDict = {}
		for year in self:
			dataDict = {}
			table = self.__getTable(year, flag, 4, 21)
			trs = table.findAll('tr')
			contentDict
			for tr in trs:
				td = tr.findAll('td')[0]
				dataDict[str(td.text)] = "http://www.basketball-reference.com" + str(td.a['href'])
			contentDict[YEARLIST[self.index(year)]] = dataDict
		return contentDict


class FinalStat(dict):
	"""Class of each year's Final game stat"""

	def __init__(self, *arglist, **argDict):
		"""Construct a FinalStat object from a """
		dict.__init__(self, *arglist, **argDict)

	def __getTable(self, url, pos):
		"""Get interested table from page.

		Arguments:
			url  -- Page's url.
			pos  -- position of the table.

		Return:
			Required table section from that page which is a BeautifulSoup object.
		"""
		connect = urllib2.urlopen(url)
		page = connect.read()
		soup = BeautifulSoup(page)
		tables = soup.findAll("table")
		connect.close()
		return tables[pos]

	def __getScoreTable(self, url, pos):
		"""Get score table's content from page.

		Arguments:
			url -- page's url.
			pos -- Since the number of each year's final game varies so that table's position varies. 
			We will count each year's game first, then calculate the right position of the table.

		Return:
			Countent of the table.
		"""
		pos = 9 + pos
		return self.__getTable(url, pos)

	def __getFourFactorTable(self, url, pos):
		pos = 10 + pos
		return self.__getTable(url, pos)

	def __getHomeTeamTable(self, url, pos):
		pos = 11 + pos
		return self.__getTable(url, pos)

	def __getAwayTeamTable(self, url, pos):
		pos = 13 + pos
		return self.__getTable(url, pos)

	def __getContentFromTable(self, cTable, flag):
		"""Get the contents from table.

		Argument:

			soupTable -- data table.

		Return:

			A list include each column's data
		"""
		trs = cTable.findAll('tr')
		retList = []
		for tr in trs[2:]:
			tds = tr.findAll("td")
			cList = []
			# if flag: tds = tds[-1]
			for td in tds:
				try:
					cList.append(float(td.text))
				except ValueError:
					cList.append(str(td.text))
			retList.append(cList)
		return retList

	def __getShortChartPageUrlDict(self):
		"""Get short chart page's url from final page's url dictionary

		Argument:
			finalPageUrlDict -- final page's url

		return:

			Short chart page's url dictionary
		"""
		urlDict = self.copy()
		for data in urlDict.values():
			for game in data.keys():
				oldUrl = data[game]
				index = oldUrl.rfind('/')
				newUrl = oldUrl[:index] + '/shot-chart' + oldUrl[index:]
				data[game] = newUrl
		return urlDict

	def __parseingLocation(self, soupTags):
		"""Get shot location from div tags extracted by BeautifulSoup

		Argument:
			soupTags --  BeautifulSoup tag object

		return:
			shot coordinate list. i.e. [{'x':1, 'y':2}]
		"""
		locationList = []
		for div in soupTags.findAll("div"):
			locDict = {}
			missedString = str(div.text)
			missedPattern = re.compile('missed')
			if missedPattern.search(missedString):
				continue
			locationString = div['style']
			positionPattern = re.compile(r'top:(\d*)px;left:(\d*)px;$')
			y, x = positionPattern.search(locationString).groups()
			locDict['y'] = int(y)
			locDict['x'] = int(x)
			locationList.append(locDict)
		return locationList


	def __getShortChartData(self, url):
		"""Get shot location from each page's url

		Argument:
			url --  shot chart page's url

		return:
			shot are coordinate dictionary. i.e. {'team':[, , ,], 'team': [, , ,]}
		"""
		connect = urllib2.urlopen(url)
		page = connect.read()
		soup = BeautifulSoup(page)
		firstTeamTags, secondTeamTags = soup.findAll("div", {'id':re.compile(r"^shots-(\d*)")})
		firstTeamName = re.compile(r'^shots-(\D*)').search(str(firstTeamTags['id'])).groups()[0]
		secondTeamName = re.compile(r'^shots-(\D*)').search(str(secondTeamTags['id'])).groups()[0]
		locationDict = {}
		locationDict[firstTeamName] = self.__parseingLocation(firstTeamTags)
		locationDict[secondTeamName] = self.__parseingLocation(secondTeamTags)
		return locationDict

	def __buildForHeatMap(self, sList):
		"""Count the occurrence of coordinate in each team's shot map data.

		Return:
			required data for heatmap.js 
		"""
		bFrozen = [frozenset(dict_item.items()) for dict_item in sList]
		x = Counter(bFrozen)
		ret, maxOccur= x.most_common(), x.most_common(1)[0][1]
		newList = []
		for item in ret:
			newDict = dict(item[0])
			newDict['count'] = item[1]
			newList.append(newDict)
		newDict = {}
		newDict['max'] = maxOccur
		newDict['data'] = newList
		return newDict

	def __getFinalShortCharts(self):
		"""Get final game's short chart coordinate.
		"""
		pageUrl = self.__getShortChartPageUrlDict()
		scDict = {}
		for year in pageUrl.keys():
			yearDict = {}
			yearData = pageUrl[year]
			for game in yearData.keys():
				url = yearData[game]
				yearDict[game] = self.__getShortChartData(url)
			scDict[year] = yearDict
		return scDict

	def __mergeEachGameData(self, scDict):
		"""Optimize data structure

		Return:
			a list of each year shot map data.
		"""
		mergedList = []
		for year in scDict.keys():
			yearDict = {}
			yearData = scDict[year]
			team_1, team_2 = yearData.values()[0].keys()[0], yearData.values()[0].keys()[1]
			temp = {}
			for data in yearData.values():
				try:
					if temp[team_1] != None:
						temp[team_1] += data[team_1]
						temp[team_2] += data[team_2]
				except KeyError:
					temp[team_1] = data[team_1]
					temp[team_2] = data[team_2]
			yearDict[year] = temp
			mergedList.append(yearDict)
		finalList = []
		for item in mergedList:
			finalDict = {}
			finalDict['year'] = item.keys()[0]
			finalDict['data'] = item.values()[0]
			finalList.append(finalDict)
		return finalList

	def __getDataForHeatMap(self, scList):
		"""Optimize data structure in order to draw heatmap using heatmap.js

		Argument:
			scDict -- each year's shot map data

		return structure sample: {'year' : 2001, 'data' : {
									'SAS' : {'max': 1, 'data' : [{'x' : 10, 'y' : 20, 'count':2}]}, 
									'LAL': {...}}
								 }
		"""
		for year in scList:
			data = year['data']
			for team in data.keys():
				data[team] = self.__buildForHeatMap(data[team])
		return scList


	def getShortCharts(self):
		"""
		Return:
			each year's final game shot map data
		"""
		temp = self.__getFinalShortCharts()
		temp_2 = self.__mergeEachGameData(temp)
		return self.__getDataForHeatMap(temp_2)

	def getStats(self):
		"""Get data from table

		Returns:

			A python dictionary including Final Game statistics.

			TODO: may be add one more get table method
		"""
		#TODO: Get all data from such 4 tables
		statDict = {}
		eachYear = {}
		for year in self.keys():
			subGameDict = self[year]
			gameCount = len(subGameDict)
			eachGame = {}
			for game in subGameDict.keys():
				eachStat = {}
				url = subGameDict[game]
				pos = 0
				if gameCount > 4:
					pos = gameCount - 4
				score = self.__getScoreTable(url, pos)
				factor = self.__getFourFactorTable(url, pos)
				home = self.__getHomeTeamTable(url, pos)
				away = self.__getAwayTeamTable(url, pos)
				eachStat['score'] = self.__getContentFromTable(score, 0)
				eachStat['Four Factor'] = self.__getContentFromTable(factor, 0)
				homeTeam = eachStat['score'][0][0]
				awayTeam = eachStat['score'][1][0]
				eachStat[homeTeam] = self.__getContentFromTable(home, 1)
				eachStat[awayTeam] = self.__getContentFromTable(away, 1)
				eachGame[game] = eachStat
			eachYear[str(year)] = eachGame
		return eachYear




