####################################################################  
# Send demographic data by zip code to csv file
#     replaced by direct insert into mysql db
####################################################################  
#
def SendNYCZipDataToCSV():
  import csv

  hhFile = open(r"C:\Users\bigpalooka\Downloads\zipinfo005c.csv","wb")
  hFile = csv.writer(hhFile)

  hFile.writerow(['zip','inc','pov','pop'])  

  #for iZip in ['10012','10024','10036','10458','10467','10468','10463','10471','10466','10469','10470','10475','10461','10462','10464','10465','10472','10473','10026','10027','10030','10037','10039','10001','10011','10018','10019','10020','10036','10029','10035','10012','10013','10014','10004','10005','10006','10007','10038','10280','10002','10003','10009','10023','10024','10025','10031','10032','10033','10034','10040','10302','10303','10310','10301','10304','10305','10314']:
  for iZip in ['10012','10024','10036']:
    print iZip

    zipList = GetZipData(iZip)
                                                       
    hFile.writerow(zipList)
  hhFile.close()


####################################################################  
# Send demographic data by zipcode to mysql db
####################################################################  
#
def SendNYCZipDataToMySQL():
  import re
  import MySQLdb as db

  conn = db.connect(user="myID",  passwd="myPWD", host="mysql11.brinkster.com", db="procyk01")
  cur = conn.cursor()

  for iZip in ['10012','10024','10036','10458','10467','10468','10463','10471','10466','10469','10470','10475','10461','10462','10464','10465','10472','10473','10026','10027','10030','10037','10039','10001','10011','10018','10019','10020','10036','10029','10035','10012','10013','10014','10004','10005','10006','10007','10038','10280','10002','10003','10009','10023','10024','10025','10031','10032','10033','10034','10040','10302','10303','10310','10301','10304','10305','10314']:
  #for iZip in ['10012','10021','10458','10467','10468']:
    print iZip
    zipList = GetZipData(iZip)
    BoroughNeighborhood = GetBoroughNeighborhoodGivenZip(iZip)
    Borough = BoroughNeighborhood[0]
    Neighborhood = BoroughNeighborhood[1]
    
    SQLFrag = "('" + Borough + "','" + Neighborhood + "','" + str(zipList[0]) + "'," + str(zipList[1]) + "," + str(zipList[2]) + "," + re.sub(r"\D","",zipList[3]) + ")"

    strSQL = 'INSERT INTO Demographics (Borough,Neighborhood,zipcode,population,poverty,income) VALUES ' + SQLFrag
    print strSQL
    #pass    
    cur.execute(strSQL)
  

####################################################################  
# Called by 2 functions (mysql and csv)
#   to get zip demographics data
####################################################################  
#
def GetZipData(iZip):
  from bs4 import BeautifulSoup
  import urllib2
  import re
  from datetime import datetime as DT

  print iZip
                                                 
  webPageLink = "http://zipskinny.com/index.php?zip=" + iZip
  webPage=urllib2.urlopen(webPageLink)
  webText = webPage.read()

  webSoup = BeautifulSoup(webText)

  for t in webSoup.findAll(text='Population: '):
    p = t.parent.parent
    pop =  p.contents[1].text
    print "pop:", pop  

  for t in webSoup.findAll(text='Below Poverty Line'):
    p = t.parent.parent
    pov =  p.contents[3].text
    pov = float(pov.replace('%',''))/100
    print "pov",pov  

  for t in webSoup.findAll(text=re.compile('Median Household Income:')):
    inc = t.string.split()[3]
    print "inc",inc  

  zipList=[str(iZip),pop,pov,inc]
  return zipList


####################################################################  
# this gets summary of complaints by neighborhood data 
#    to send to mySQL db
####################################################################  
def SendNYCComplaintsByZipToMySQL():
  import MySQLdb as db
  import re
  import urllib2
  from datetime import datetime as DT

  conn = db.connect(user="myID",  passwd="myPWD", host="mysql11.brinkster.com", db="procyk01")
  conn.autocommit(True)
  cur = conn.cursor()
  strSQL = "INSERT INTO complaints (complaintdate,borough,neighborhood,complaint,CT) VALUES "
  
  ### for each month in year 2012 - uncomment this code  #########
  #for imonth in range(1,13):
  #  if imonth==12:
  #    strMonth="12/2012"
  #    strFullMonth="12/1/2012"
  #    crdate = "(created_date>'2012-12-01'+AND+created_date<'2013-01-01')"
  #  else:
  #    strMonth=str(imonth)+"/2012"
  #    strFullMonth=str(imonth)+"/1/2012"
  #    crdate = "(created_date>'2012-"+('0'+str(imonth) if imonth<10 else str(imonth))+ "-01'+AND+created_date<'2012-"+('0'+str(imonth+1) if imonth+1<10 else str(imonth+1))+"-01')"
  ################################################################
  
  
  ### for each month in year 2013 - uncomment this code  #########
  for imonth in range(4,5):
    if imonth==12:
      strMonth="12/2013"
      strFullMoth="12/1/2013"
      crdate = "(created_date>'2013-12-01'+AND+created_date<'2014-01-01')"
    else:
      strMonth=str(imonth)+"/2013"
      strFullMonth=str(imonth)+"/1/2013"
      crdate = "(created_date>'2013-"+('0'+str(imonth) if imonth<10 else str(imonth))+ "-01'+AND+created_date<'2013-"+('0'+str(imonth+1) if imonth+1<10 else str(imonth+1))+"-01')"
  #################################################################

    for i in range(1,21):
      zipData = GetBoroughNeighborhoodZipstring(i)
      borough = zipData[0]               
      neighborhood = zipData[1]
      zipstring = zipData[2]

      webPageLink = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv?$query=select+complaint_type,count(complaint_type)+AS+CT+where"  #+(created_date>'2013-03-01'+AND+created_date<'2013-04-09')+and+(incident_zip='10012'+OR+incident_zip='10024')+GROUP+BY+complaint_type"
      webPageLink += "+" + crdate + "+AND+" + zipstring + "+GROUP+BY+complaint_type"
      
      print webPageLink
      webPage=urllib2.urlopen(webPageLink)
  
      for row in webPage:
        aVal=row.split(',')
        aVal2=aVal[1].split('\n')
        if aVal2[0].isdigit():
          strDate = DT.strftime(DT.strptime(strFullMonth, "%m/%d/%Y"),"%Y-%m-%d")
          sqlFrag = " ('" + str(strDate) + "','" + str(borough) + "','" + str(neighborhood) + "','" + str(aVal[0]) + "'," + str(aVal2[0]) + ");"
          print strSQL + sqlFrag
          #cur.execute(strSQL + sqlFrag)
          pass

      
####################################################################  
# this gets detail data and sends it to csv file 
#    used by Tableau
####################################################################  
#
def SendNYCComplaintsDetailsByZipToCSV():
  #from bs4 import BeautifulSoup
  import re
  import urllib2
  from datetime import datetime as DT
  import csv

  #open file for appending, binary "ab"  -  csv files should be written as binary files
  hhFile = open(r"C:\Users\bigpalooka\Downloads\ComplaintDetailsOct2012.csv","ab")
  hFile = csv.writer(hhFile)
  
  strMonth = "10/2012"
  strFullMonth = "10/01/2012"  
  crdate = "(created_date>'2012-10-01'+AND+created_date<'2012-11-01')"  

  # there is a limit of 1000 records for each query.
  # Have to use limit and offset to get 1000 records at a time.
  
  iLimit = 1000

  for iOffset in range(0,6000,iLimit):
    strPaging = "+limit+" + str(iLimit) + "+offset+" + str(iOffset) 
 


    ### for each month in year 2012 - uncomment this code  ################################
    #for imonth in range(12,13):
    #  if imonth==12:
    #    strMonth="12/2012"
    #    strFullMonth="12/1/2012"
    #    crdate = "(created_date>'2012-12-01'+AND+created_date<'2013-01-01')"
    #  else:
    #    strMonth=str(imonth)+"/2012"
    #    strFullMonth=str(imonth)+"/1/2012"
    #    crdate = "(created_date>'2012-"+('0'+str(imonth) if imonth<10 else str(imonth))+ "-01'+AND+created_date<'2012-"+('0'+str(imonth+1) if imonth+1<10 else str(imonth+1))+"-01')"
    ################################################################


    ### for each month in year 2013 - uncomment this code  ################################
    #for imonth in range(1,5):
    #  if imonth==12:
    #    strMonth="12/2013"
    #    strFullMoth="12/1/2013"
    #    crdate = "(created_date>'2013-12-01'+AND+created_date<'2014-01-01')"
    #  else:
    #    strMonth=str(imonth)+"/2013"
    #    strFullMonth=str(imonth)+"/1/2013"
    #    crdate = "(created_date>'2013-"+('0'+str(imonth) if imonth<10 else str(imonth))+ "-01'+AND+created_date<'2013-"+('0'+str(imonth+1) if imonth+1<10 else str(imonth+1))+"-01')"
    #################################################################

    for i in range(1,21):
      zipData = GetBoroughNeighborhoodZipstring(i)
      borough = zipData[0]               
      neighborhood = zipData[1]
      zipstring = zipData[2]

      webPageLink = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv?$query=select+created_date,complaint_type,incident_zip,latitude,longitude+where"  #+(created_date>'2013-03-01'+AND+created_date<'2013-04-09')+and+(incident_zip='10012'+OR+incident_zip='10024')+GROUP+BY+complaint_type"
      webPageLink += "+" + crdate + "+AND+" + zipstring + strPaging    
      
      print webPageLink
      webPage=urllib2.urlopen(webPageLink)
  
      for row in webPage:
        aVal=row.split(',')
        aVal4=aVal[4].split('\n')  # get the value before the "\n" in aVal[4] 
        hFile.writerow([strFullMonth,borough,neighborhood,aVal[0],aVal[1],aVal[2],aVal[3],aVal4[0]])
      
  hhFile.close()


####################################################################  
# Function to fetch query fragment strings 
#    for queries to nyc open data
####################################################################  
#
def GetBoroughNeighborhoodZipstring(i):
    if i==1:
      borough = "Manhattan"
      neighborhood = "East Harlem"          
      zipstring="(incident_zip='10029'+OR+incident_zip='10030'+OR+incident_zip='10035'+OR+incident_zip='10039')"
    elif i==2:
      borough = "Manhattan"
      neighborhood = "Central Harlem"         
      zipstring="(incident_zip='10026'+OR+incident_zip='10027'+OR+incident_zip='10037')"
    elif i==3:
      borough = "Manhattan"
      neighborhood = "GramercyPark + Murray Hill"          
      zipstring="(incident_zip='10010'+OR+incident_zip='10016'+OR+incident_zip='10017'+OR+incident_zip='10022')"
    elif i==4:
      borough = "Manhattan"
      neighborhood = "Upper East Side"          
      zipstring="(incident_zip='10021'+OR+incident_zip='10028'+OR+incident_zip='10044'+OR+incident_zip='10028')"
    elif i==5:
      borough = "Manhattan"
      neighborhood = "Chelsea + Clinton"          
      zipstring="(incident_zip='10001'+OR+incident_zip='10011'+OR+incident_zip='10018'+OR+incident_zip='10019'+OR+incident_zip='10020'+OR+incident_zip='10036')"
    elif i==6:
      borough = "Manhattan"
      neighborhood = "Greenwich Village + Soho"
      zipstring="(incident_zip='10012'+OR+incident_zip='10013'+OR+incident_zip='10014')"
    elif i==7:
      borough = "Manhattan"
      neighborhood = "Lower Manhattan"
      zipstring="(incident_zip='10004'+OR+incident_zip='10005'+OR+incident_zip='10006'+OR+incident_zip='10007'+OR+incident_zip='10038'+OR+incident_zip='10280')"
    elif i==8:
      borough = "Manhattan"
      neighborhood = "Lower East Side"
      zipstring="(incident_zip='10002'+OR+incident_zip='10003'+OR+incident_zip='10009')"
    elif i==9:
      borough = "Manhattan"
      neighborhood = "Upper West Side"
      zipstring="(incident_zip='10023'+OR+incident_zip='10024'+OR+incident_zip='10025')"
    elif i==10:
      borough = "Manhattan"
      neighborhood = "Inwood + Washington Heights"
      zipstring="(incident_zip='10031'+OR+incident_zip='10032'+OR+incident_zip='10033'+OR+incident_zip='10034'+OR+incident_zip='10040')"

    elif i==11:
      borough = "Bronx"
      neighborhood = "Morrisania + High Bridge"          
      zipstring="(incident_zip='10451'+OR+incident_zip='10452'+OR+incident_zip='10456')"
    elif i==12:
      borough = "Bronx"
      neighborhood = "Hunts Point + Longwood"          
      zipstring="(incident_zip='10454'+OR+incident_zip='10455'+OR+incident_zip='10459'+OR+incident_zip='10474')"
    elif i==13:
      borough = "Bronx"
      neighborhood = "Bronx Park + Fordham"
      zipstring="(incident_zip='10458'+OR+incident_zip='10467'+OR+incident_zip='10468')"
    elif i==14:
      borough = "Bronx"
      neighborhood = "Kingsbridge + Riverdale"
      zipstring="(incident_zip='10463'+OR+incident_zip='10471')"
    elif i==15:
      borough = "Bronx"
      neighborhood = "Northeast Bronx"
      zipstring="(incident_zip='10466'+OR+incident_zip='10469'+OR+incident_zip='10470'+OR+incident_zip='10475')"
    elif i==16:
      borough = "Bronx"
      neighborhood = "Southeast Bronx"
      zipstring="(incident_zip='10461'+OR+incident_zip='10462]'+OR+incident_zip='10464'+OR+incident_zip='10465'+OR+incident_zip='10472'+OR+incident_zip='10473')"

    elif i==17:
      borough = "Staten Island"
      neighborhood = "South Shore"          
      zipstring="(incident_zip='10306'+OR+incident_zip='10307'+OR+incident_zip='10308'+OR+incident_zip='10309'+OR+incident_zip='10312')"
    elif i==18:
      borough = "Staten Island"
      neighborhood = "Port Richmond"
      zipstring="(incident_zip='10302'+OR+incident_zip='10303'+OR+incident_zip='10310')"
    elif i==19:
      borough = "Staten Island"
      neighborhood = "Stapleton + St. George"
      zipstring="(incident_zip='10301'+OR+incident_zip='10304'+OR+incident_zip='10305')"
    elif i==20:
      borough = "Staten Island"
      neighborhood = "Mid-Island"
      zipstring="(incident_zip='10314')" 
    
    return [borough,neighborhood,zipstring]
    

####################################################################  
#  Take zipcode input, return borough and neighborhood
#     used by functions writing to mysql
####################################################################  
#  
def GetBoroughNeighborhoodGivenZip(iZip):
    if iZip in ['10029','10030','10035','10039']:
      Borough = "Manhattan"
      Neighborhood = "East Harlem"          
    elif iZip in ['10026','10027','10037']:
      Borough = "Manhattan"
      Neighborhood = "Central Harlem"         
    elif iZip in ['10010','10016','10017','10022']:
      Borough = "Manhattan"
      Neighborhood = "GramercyPark + Murray Hill"          
    elif iZip in ['10021','10028','10044','10028']:
      Borough = "Manhattan"
      Neighborhood = "Upper East Side"          
    elif iZip in ['10001','10011','10018','10019','10020','10036'] :
      Borough = "Manhattan"
      Neighborhood = "Chelsea + Clinton"          
    elif iZip in ['10012','10013','10014']:
      Borough = "Manhattan"
      Neighborhood = "Greenwich Village + Soho"
    elif iZip in ['10004','10005','10006','10007','10038','10280']:
      Borough = "Manhattan"
      Neighborhood = "Lower Manhattan"
    elif iZip in ['10002','10003','10009']:
      Borough = "Manhattan"
      Neighborhood = "Lower East Side"
    elif iZip in ['10023','10024','10025']:
      Borough = "Manhattan"
      Neighborhood = "Upper West Side"
    elif iZip in ['10031','10032','10033','10034','10040']:
      Borough = "Manhattan"
      Neighborhood = "Inwood + Washington Heights"

    elif iZip in ['10451','10452','10456']:
      Borough = "Bronx"
      Neighborhood = "Morrisania + High Bridge"          
    elif iZip in ['10454','10455','10459','10474']:
      Borough = "Bronx"
      Neighborhood = "Hunts Point + Longwood"          
    elif iZip in ['10458','10467','10468']:
      Borough = "Bronx"
      Neighborhood = "Bronx Park + Fordham"
    elif iZip in ['10463','10471']:
      Borough = "Bronx"
      Neighborhood = "Kingsbridge + Riverdale"
    elif iZip in ['10466','10469','10470','10475']:
      Borough = "Bronx"
      Neighborhood = "Northeast Bronx"
    elif iZip in ['10461','10462]','10464','10465','10472','10473']:
      Borough = "Bronx"
      Neighborhood = "Southeast Bronx"

    elif iZip in ['10306','10307','10308','10309','10312']:
      Borough = "Staten Island"
      Neighborhood = "South Shore"          
    elif iZip in ['10302','10303','10310']:
      Borough = "Staten Island"
      Neighborhood = "Port Richmond"
    elif iZip in ['10301','10304','10305']:
      Borough = "Staten Island"
      Neighborhood = "Stapleton + St. George"
    elif iZip in ['10314'] :
      Borough = "Staten Island"
      Neighborhood = "Mid-Island"

    return [Borough,Neighborhood]




def test1():
  i=1
  if i<10:
    stri = '0' + str(i)
  else:
    stri= str(i)
  print i, stri
  
  strj='0'+str(i) if i<10 else str(i)
  print strj


def test2():
  a="abc,def"
  b= a.split(',')
  print b[0],b[1]


def test3():
  a='$3,500'
  #b=a[1:10]
  print a[1:10]
  

if __name__ == "__main__":
  #SendNYCComplaintsByZipToMySQL()
  #SendNYCZipDataToMySQL()
  #GetNYCComplaintsDetailsByZip()
  
  #SendNYCZipDataToCSV()
  #GetNYCComplaintsB()
  #test1()
  #test2()
  #test3()
  #SendNYCZipDataToMySQL()
  pass
