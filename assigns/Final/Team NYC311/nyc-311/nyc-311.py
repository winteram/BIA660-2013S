#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import json
import os
import cgi
from google.appengine.ext import db
from google.appengine.api import rdbms
import csv 


_INSTANCE_NAME = "bia660-nyc-311:nyc311database"

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class MainPage(webapp2.RequestHandler):
	def get(self):
		

		print "GET METHOD"
		template = JINJA_ENVIRONMENT.get_template('nyc-311.html')

		self.response.write(template.render())

		
		

class ComplaintData(webapp2.RequestHandler):
	def post(self):
		print "POST METHOD"
		conn = rdbms.connect( instance=_INSTANCE_NAME, database="bia660nyc")
		cursor = conn.cursor()
		viz_name = self.request.get('viz_name')
		if viz_name=='barchart':
			selectedname1 = self.request.get('selectedname')
			selecteddate = self.request.get('selecteddate')+'-01'
			Matrix = [[0 for x in xrange(2)] for x in xrange(11)]
			Matrix[0] = ["complaints","number"]
			
			cursor.execute("select complaint, CT from complaints where neighborhood='"+selectedname1+"' and complaintdate='"+selecteddate+"' order by CT desc limit 10" )
			i=1
			for row in cursor.fetchall():
				Matrix[i]=[row[0],row[1]]
				i=i+1
			conn.close()
			return self.response.write(json.dumps(Matrix))
		if viz_name=='linechart':
			selectedname1 = self.request.get('selectedname1')
			selectedname2 = self.request.get('selectedname2')
			Matrix2 =[]
			Matrix3 =[]
			Matrix2.append(["Date",selectedname1])
			Matrix3.append(selectedname2)
			cursor.execute("select complaintdate,neighborhood,SUM(CT) from complaints where neighborhood='"+selectedname1+"' group by complaintdate,neighborhood")
			for row in cursor.fetchall():
				Matrix2.append([str(row[0]),row[2]])
			cursor.execute("select complaintdate,neighborhood,SUM(CT) from complaints where neighborhood='"+selectedname2+"' group by complaintdate,neighborhood")
			for row in cursor.fetchall():
				Matrix3.append(row[2])
			i=0
			for row in Matrix2:
				row.append(Matrix3[i])
				i=i+1
			conn.close()
			return self.response.write(json.dumps(Matrix2))
		
		
		
class DemographicsData(webapp2.RequestHandler):
	def post(self):
		print "POST METHOD2"
		selectedname1 = self.request.get('selectedname')
		conn = rdbms.connect( instance=_INSTANCE_NAME, database="bia660nyc")
		cursor = conn.cursor()
		cursor.execute("select * from demographics where Neighborhood='"+selectedname1+"'")
		Matrix=[]
		for row in cursor.fetchall():
			Matrix.append([row[2], row[3], row[4]*100, row[5]])
		conn.close()
		return self.response.write(json.dumps(Matrix))

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/loadBarchart', ComplaintData),
	('/loadTable', DemographicsData)
], debug=True)
