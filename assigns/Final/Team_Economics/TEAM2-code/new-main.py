import os
import cgi
import urllib
import logging
import datetime
import webapp2
import csv
import simplejson

from google.appengine.api import rdbms
from google.appengine.ext import db

import jinja2

template_path = os.path.join(os.path.dirname(__file__))

jinja2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_path))  

class occ_data(db.Model):
    occ_code = db.StringProperty()
    occ_title = db.StringProperty()
    occ_group = db.StringProperty()
    a_mean = db.StringProperty()
    occ_major = db.StringProperty()
    
class economy_data(db.Model):
    Country = db.StringProperty()
    Subject_code = db.StringProperty()
    y_1980 = db.StringProperty()
    y_1981 = db.StringProperty()
    y_1982 = db.StringProperty()
    y_1983 = db.StringProperty()
    y_1984 = db.StringProperty()
    y_1985 = db.StringProperty()
    y_1986 = db.StringProperty()
    y_1987 = db.StringProperty()
    y_1988 = db.StringProperty()
    y_1989 = db.StringProperty()
    y_1990 = db.StringProperty()
    y_1991 = db.StringProperty()
    y_1992 = db.StringProperty()
    y_1993 = db.StringProperty()
    y_1994 = db.StringProperty()
    y_1995 = db.StringProperty()
    y_1996 = db.StringProperty()
    y_1997 = db.StringProperty()
    y_1998 = db.StringProperty()
    y_1999 = db.StringProperty()
    y_2000 = db.StringProperty()
    y_2001 = db.StringProperty()
    y_2002 = db.StringProperty()
    y_2003 = db.StringProperty()
    y_2004 = db.StringProperty()
    y_2005 = db.StringProperty()
    y_2006 = db.StringProperty()
    y_2007 = db.StringProperty()
    y_2008 = db.StringProperty()
    y_2009 = db.StringProperty()
    y_2010 = db.StringProperty()
    y_2011 = db.StringProperty()
    y_2012 = db.StringProperty()
    y_2013 = db.StringProperty()
    y_2014 = db.StringProperty()
    y_2015 = db.StringProperty()
    y_2016 = db.StringProperty()
    y_2017 = db.StringProperty()
    y_2018 = db.StringProperty()

class jobopens(db.Model):
    title = db.StringProperty()
    year = db.StringProperty()
    month = db.StringProperty()
    value = db.StringProperty()
    
class jobhires(db.Model):
    title = db.StringProperty()
    year = db.StringProperty()
    month = db.StringProperty()
    value = db.StringProperty()

                
class MainHandler(webapp2.RequestHandler):
    def get(self):
#         db.delete(occ_data.all())
#         db.delete(jobhires.all())
#         db.delete(jobopens.all())
#         db.delete(economy_data.all())
#     
#         occ = open('2012 annual income for positions.csv')
#         occ.readline()
#         reader_occ = csv.reader(occ)
#         for o1, o2, o3, o4, o5 in reader_occ:
#             tem_occ = occ_data(occ_code = o1,
#                               occ_title = o2,
#                               occ_group = o3,
#                               a_mean = o4,
#                               occ_major = o5)
#             tem_occ.put()
#                 
#         jobopen = open('jobsopen.csv')
#         jobopen.readline()
#         reader_jobopen = csv.reader(jobopen)
#         for jo1, jo2, jo3, jo4 in reader_jobopen:
#             tem_jo = jobopens(title = jo1,
#                                   year = jo2,
#                                   month = jo3,
#                                   value = jo4)
#             tem_jo.put()
#                 
#         jobhire = open('jobshire.csv')
#         jobhire.readline()
#         reader_jobhire = csv.reader(jobhire)
#         for jh1, jh2, jh3, jh4 in reader_jobhire:           
#             tem_jh = jobhires(title = jh1,
#                                   year = jh2,
#                                   month = jh3,
#                                   value = jh4)
#             tem_jh.put()
#                    
#         economy = open('GDP.csv')
#         economy.readline()
#         reader = csv.reader(economy)
#         for c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40,c41 in reader:
#             tem = economy_data(Country = c2,
#                                    Subject_code = c1,
#                                    y_1980 = c3,
#                                    y_1981 = c4,
#                                    y_1982 = c5,
#                                    y_1983 = c6,
#                                    y_1984 = c7,
#                                    y_1985 = c8,
#                                    y_1986 = c9,
#                                    y_1987 = c10,
#                                    y_1988 = c11,
#                                    y_1989 = c12,
#                                    y_1990 = c13,
#                                    y_1991 = c14,
#                                    y_1992 = c15,
#                                    y_1993 = c16,
#                                    y_1994 = c17,
#                                    y_1995 = c18,
#                                    y_1996 = c19,
#                                    y_1997 = c20,
#                                    y_1998 = c21,
#                                    y_1999 = c22,
#                                    y_2000 = c23,
#                                    y_2001 = c24,
#                                    y_2002 = c25,
#                                    y_2003 = c26,
#                                    y_2004 = c27,
#                                    y_2005 = c28,
#                                    y_2006 = c29,
#                                    y_2007 = c30,
#                                    y_2008 = c31,
#                                    y_2009 = c32,
#                                    y_2010 = c33,
#                                    y_2011 = c34,
#                                    y_2012 = c35,
#                                    y_2013 = c36,
#                                    y_2014 = c37,
#                                    y_2015 = c38,
#                                    y_2016 = c39,
#                                    y_2017 = c40,
#                                    y_2018 = c41)
#                      
#             tem.put()                       
    
                    
            occ_list = []
    
            q = occ_data.gql("WHERE occ_major = 'major'")
    
            for title in q:
                temp = {'code':title.occ_code,'occ_title':title.occ_title,'occ_group':title.occ_group,'a_mean':title.a_mean}
                occ_list.append(temp)
    
            occ_list_value = {
                'occ_list': occ_list
            }
    
            template = jinja2_env.get_template('index.html')                          
            self.response.out.write(template.render(occ_list_value))        



def gql_json_parser(query_obj):
    result = []

    for entry in query_obj:
        result.append(dict([(p, unicode(getattr(entry, p))) for p in entry.properties()]))
    return result

class DC(webapp2.RequestHandler):
    def get(self):
        ge = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'Germany')
        us = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'United States')
        uk = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'United Kingdom')
        jp = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'Japan')
        
        
        ge_values = gql_json_parser(ge)
        us_values = gql_json_parser(us)
        uk_values = gql_json_parser(uk)
        jp_values = gql_json_parser(jp)        
        
        dict = []            
        map = {"country":'', "data":[]}         
        for data in ge_values:
            map["country"] = "Germany"
            map["data"].append(float(data["y_2012"]))
            map["data"].append(float(data["y_2013"]))
            map["data"].append(float(data["y_2014"]))
            map["data"].append(float(data["y_2015"]))
            map["data"].append(float(data["y_2016"]))
            map["data"].append(float(data["y_2017"]))
            map["data"].append(float(data["y_2018"]))           
            dict.append(map)  
            break     
        map_us = {"country":'', "data":[]}   
        logging.info("%s", map_us)
        for us_data in us_values:
            map_us["country"] = "US"
            map_us["data"].append(float(us_data["y_2012"]))
            map_us["data"].append(float(us_data["y_2013"]))
            map_us["data"].append(float(us_data["y_2014"]))
            map_us["data"].append(float(us_data["y_2015"]))
            map_us["data"].append(float(us_data["y_2016"]))
            map_us["data"].append(float(us_data["y_2017"]))
            map_us["data"].append(float(us_data["y_2018"]))
            dict.append(map_us)       
            break
        map_uk = {"country":'', "data":[]}   
        for uk_data in uk_values:
            map_uk["country"] = "UK"
            map_uk["data"].append(float(uk_data["y_2012"]))
            map_uk["data"].append(float(uk_data["y_2013"]))
            map_uk["data"].append(float(uk_data["y_2014"]))
            map_uk["data"].append(float(uk_data["y_2015"]))
            map_uk["data"].append(float(uk_data["y_2016"]))
            map_uk["data"].append(float(uk_data["y_2017"]))
            map_uk["data"].append(float(uk_data["y_2018"]))
            
            dict.append(map_uk)       
            break
        map_jp = {"country":'', "data":[]}   
        for jp_data in jp_values:
            map_jp["country"] = "Japan"
            map_jp["data"].append(float(jp_data["y_2012"]))
            map_jp["data"].append(float(jp_data["y_2013"]))
            map_jp["data"].append(float(jp_data["y_2014"]))
            map_jp["data"].append(float(jp_data["y_2015"]))
            map_jp["data"].append(float(jp_data["y_2016"]))
            map_jp["data"].append(float(jp_data["y_2017"]))
            map_jp["data"].append(float(jp_data["y_2018"]))
            
            dict.append(map_jp)       
            break
        jd = simplejson.dumps(dict)                           
        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(jd)

class DingC(webapp2.RequestHandler):
    def get(self):
        cn = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'China')
        ru = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'Russia')
        br = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'Brazil')
        id = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'India')
        
        
        cn_values = gql_json_parser(cn)
        ru_values = gql_json_parser(ru)
        br_values = gql_json_parser(br)
        id_values = gql_json_parser(id)        
        
        dict = []            
        map = {"country":'', "data":[]}         
        for data in cn_values:
            map["country"] = "China"
            map["data"].append(float(data["y_2012"]))
            map["data"].append(float(data["y_2013"]))
            map["data"].append(float(data["y_2014"]))
            map["data"].append(float(data["y_2015"]))
            map["data"].append(float(data["y_2016"]))
            map["data"].append(float(data["y_2017"]))
            map["data"].append(float(data["y_2018"]))
            
            dict.append(map)  
            break                 
        map_ru = {"country":'', "data":[]}   
        for ru_data in ru_values:
            map_ru["country"] = "Russia"
            map_ru["data"].append(float(ru_data["y_2012"]))
            map_ru["data"].append(float(ru_data["y_2013"]))
            map_ru["data"].append(float(ru_data["y_2014"]))
            map_ru["data"].append(float(ru_data["y_2015"]))
            map_ru["data"].append(float(ru_data["y_2016"]))
            map_ru["data"].append(float(ru_data["y_2017"]))
            map_ru["data"].append(float(ru_data["y_2018"]))

            dict.append(map_ru)       
            break

        map_br = {"country":'', "data":[]}   
        for br_data in br_values:
            map_br["country"] = "Brazil"
            map_br["data"].append(float(br_data["y_2012"]))
            map_br["data"].append(float(br_data["y_2013"]))
            map_br["data"].append(float(br_data["y_2014"]))
            map_br["data"].append(float(br_data["y_2015"]))
            map_br["data"].append(float(br_data["y_2016"]))
            map_br["data"].append(float(br_data["y_2017"]))
            map_br["data"].append(float(br_data["y_2018"]))
            
            dict.append(map_br)       
            break

        map_id = {"country":'', "data":[]}   
        for id_data in id_values:
            map_id["country"] = "India"
            map_id["data"].append(float(id_data["y_2012"]))
            map_id["data"].append(float(id_data["y_2013"]))
            map_id["data"].append(float(id_data["y_2014"]))
            map_id["data"].append(float(id_data["y_2015"]))
            map_id["data"].append(float(id_data["y_2016"]))
            map_id["data"].append(float(id_data["y_2017"]))
            map_id["data"].append(float(id_data["y_2018"]))
            
            dict.append(map_id)       
            break

        jd = simplejson.dumps(dict)                           
        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(jd)
        
class UC(webapp2.RequestHandler):
    def get(self):
        af = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'Afghanistan')
        ir = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'Iraq')
        rw = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'Rwanda')
        ug = db.GqlQuery("SELECT * FROM economy_data WHERE Subject_code = :1 AND Country = :2", 'NGDP_RPCH', 'Uganda')
        
        
        af_values = gql_json_parser(af)
        ir_values = gql_json_parser(ir)
        rw_values = gql_json_parser(rw)
        ug_values = gql_json_parser(ug)        
        
        dict = []            
        map = {"country":'', "data":[]}         
        for data in af_values:
            map["country"] = "Afghanistan"
            map["data"].append(float(data["y_2012"]))
            map["data"].append(float(data["y_2013"]))
            map["data"].append(float(data["y_2014"]))
            map["data"].append(float(data["y_2015"]))
            map["data"].append(float(data["y_2016"]))
            map["data"].append(float(data["y_2017"]))
            map["data"].append(float(data["y_2018"]))
            
            dict.append(map)  
            break
                
        map_ir = {"country":'', "data":[]}   
        for ir_data in ir_values:
            map_ir["country"] = "Iraq"
            map_ir["data"].append(float(ir_data["y_2012"]))
            map_ir["data"].append(float(ir_data["y_2013"]))
            map_ir["data"].append(float(ir_data["y_2014"]))
            map_ir["data"].append(float(ir_data["y_2015"]))
            map_ir["data"].append(float(ir_data["y_2016"]))
            map_ir["data"].append(float(ir_data["y_2017"]))
            map_ir["data"].append(float(ir_data["y_2018"]))
            
            dict.append(map_ir)       
            break

        map_rw = {"country":'', "data":[]}   
        for rw_data in rw_values:
            map_rw["country"] = "Rwanda"
            map_rw["data"].append(float(rw_data["y_2012"]))
            map_rw["data"].append(float(rw_data["y_2013"]))
            map_rw["data"].append(float(rw_data["y_2014"]))
            map_rw["data"].append(float(rw_data["y_2015"]))
            map_rw["data"].append(float(rw_data["y_2016"]))
            map_rw["data"].append(float(rw_data["y_2017"]))
            map_rw["data"].append(float(rw_data["y_2018"]))
            
            dict.append(map_rw)       
            break

        map_ug = {"country":'', "data":[]}   
        for ug_data in ug_values:
            map_ug["country"] = "Uganda"
            map_ug["data"].append(float(ug_data["y_2012"]))
            map_ug["data"].append(float(ug_data["y_2013"]))
            map_ug["data"].append(float(ug_data["y_2014"]))
            map_ug["data"].append(float(ug_data["y_2015"]))
            map_ug["data"].append(float(ug_data["y_2016"]))
            map_ug["data"].append(float(ug_data["y_2017"]))
            map_ug["data"].append(float(ug_data["y_2018"]))
            
            dict.append(map_ug)       
            break

        jd = simplejson.dumps(dict)                           
        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(jd)
        
class jobs(webapp2.RequestHandler):
    def get(self):
        hire_code = self.request.get('code')
        year = self.request.get('year')
        
        if hire_code == "JTU51000000HIL   ":
            open_code = "JTU51000000JOL   "
        elif hire_code == "JTU51009900HIL   ":
            open_code = "JTU51009900JOL   "
        elif hire_code == "JTU52000000HIL   ":
            open_code = "JTU52000000JOL   "
        elif hire_code == "JTU23000000HIL   ":
            open_code = "JTU23000000JOL   "
        elif hire_code == "JTU30000000HIL   ":
            open_code = "JTU30000000JOL   "
        elif hire_code == "JTU54009900HIL   ":
            open_code = "JTU54009900JOL   "
            
        logging.info("###%s, %s",open_code, hire_code)
        
        opens = db.GqlQuery("SELECT * FROM jobopens WHERE title = :1 AND year = :2 ORDER BY month", open_code, year)
        hires = db.GqlQuery("SELECT * FROM jobhires WHERE title = :1 AND year = :2 ORDER BY month", hire_code, year)         
        
#         logging.info("!!!%s", opens[0].value)
        opens_value = gql_json_parser(opens)
        hires_value = gql_json_parser(hires)
        
        jobs_dict = []
        
        map_opens = {"value":[]}
        map_hires = {"value":[]}
        for open_data in opens_value:
            map_opens["value"].append(float(open_data["value"]))
        for hire_data in hires_value:
            if hire_data["month"] != "M13":
                map_hires["value"].append(float(hire_data["value"]))
            
        jobs_dict.append(map_opens)
        jobs_dict.append(map_hires)
        
        jobsdata = simplejson.dumps(jobs_dict)
            
        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(jobsdata)   
        
class occupation_salary(webapp2.RequestHandler):
    def get(self,value):
        logging.info("in the class!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        a = value
        logging.info("the value is: "+a)
        occupation_detail = []
        first_two_digit = a.split('-')
        each_occ = occ_data.gql("WHERE occ_group = :b", b=first_two_digit[0])

        occ_json = gql_json_parser(each_occ)
        
        jd = simplejson.dumps(occ_json)
        logging.info(jd)
        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(jd)         


app = webapp2.WSGIApplication(
    [
        ("/", MainHandler),
        ("/DC", DC),
        ("/DingC", DingC),
        ("/UC", UC),
        ("/jobs", jobs),
        (r'/([0-9]{2}\-[0-9]{4})',occupation_salary)
    ],
    debug=True
)