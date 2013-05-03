import re
import urllib2
import urllib
from bs4 import BeautifulSoup
import simplejson
import json

teamList = []
teamList2 = []
Dict = {}
Dict2 = {}
Dict3 = {}
Dict4 = {}
Dict5 = {}
Dict6 = {}
Dict7 = {}
Dict8 = {}
Dict9 = {}
Dict10 = {}
Dict11 = {}
atrib = ['Played','Won','Draw','Loss','Goals Scored','Goals Conceded','Goal Different','Goal Scored per Game','Goal Conceded per Game','Win%','Total Goals Scored','Home Goals Scored','Away Goals Scored']
atrib2 = ['Home Goals Scored per Game','Home Goals Conceded per Game','Away Goals Scored per Game','Away Goals Conceded per Game','Home Win%','Away Win%','Goal Different','Rank','Pts','Won Home']
AvgW = []
AvgF = []
AvgA = []
AvgWH = []
AvgWA = []
AvgFH = []
AvgFA = []
AvgAH = []
AvgAA = []
total = 0
Htotal = 0
Atotal = 0

def leagueTable(url):
    i=0
    page = urllib.urlopen(url).read()
    soup = BeautifulSoup(page)
    table = soup.find("table")
    trs = table.findAll('td', text=re.compile('[a-z0-9A-Z]'))
    for em in trs[23:]:
        v = em.text
        teamList.append(str(v.strip()))
    for i in range (0, 20):
        teamList2.append(str(teamList[i]))
    return teamList    

def getAvgs(teamList):
    i = 0
    while i < len(teamList):
        sumh = float(teamList[i+8])+float(teamList[i+9])+float(teamList[i+10])
        suma = float(teamList[i+13])+float(teamList[i+14])+float(teamList[i+15])
        avgw = float(teamList[i+3])/float(teamList[i+2])
        avgwh = float(teamList[i+8])/sumh
        avgwa = float(teamList[i+13])/suma
        avgf = float(teamList[i+6])/float(teamList[i+2])
        avgfh = float(teamList[i+11])/sumh
        avgfa = float(teamList[i+16])/suma
        avga = float(teamList[i+7])/float(teamList[i+2])
        avgah = float(teamList[i+12])/sumh
        avgaa = float(teamList[i+17])/suma
        AvgW.append(avgw)
        AvgWH.append(avgwh)
        AvgWA.append(avgwa)
        AvgF.append(avgf)
        AvgFH.append(avgfh)
        AvgFA.append(avgfa)
        AvgA.append(avga)
        AvgAH.append(avgah)
        AvgAA.append(avgaa)
        i += 20
    return AvgW,AvgWH,AvgWA,AvgF,AvgFH,AvgFA,AvgA,AvgAH,AvgAA

def Totals(teamList):
    i = 0
    global total
    global Htotal
    global Atotal
    while i< len(teamList):
        total += int(teamList[i+6])
        Htotal += int(teamList[i+11])
        Atotal += int(teamList[i+16])
        i += 20
    print total
    return total,Htotal,Atotal
def Sprint():
    for em in teamList:
        print str(em)

def AllDict(teamList2,teamList,AvgW,AvgWH,AvgWA,AvgF,AvgFH,AvgFA,AvgA,AvgAH,AvgAA,total,Htotal,Atotal,year):
    i = 0
    Dict[str(year)] = {}
    Dict2[str(year)] = {}
    Dict3[str(year)] = {}
    Dict4[str(year)] = {}
    Dict5[str(year)] = {}
    Dict6[str(year)] = {}
    Dict7[str(year)] = {}
    Dict8[str(year)] = {}
    Dict9[str(year)] = {}
    Dict10[str(year)] = {}
    Dict11[str(year)] = {}
    while i < len(teamList2):        
        Dict7[str(year)][atrib2[8]] = teamList2[i+19]
        Dict8[str(year)][atrib[1]] = teamList2[i+3]
        Dict9[str(year)][atrib2[9]] = teamList2[i+8]
        Dict10[str(year)][atrib[4]] = teamList2[i+6]
        Dict11[str(year)][atrib[11]] = teamList2[i+11]
        i += 20
    
    while i < len(teamList):
        Dict2[str(year)][teamList[i+1]] = {}
        Dict3[str(year)][teamList[i+1]] = {}
        Dict4[str(year)][teamList[i+1]] = {}
        Dict5[str(year)][teamList[i+1]] = {}
        Dict6[str(year)][teamList[i+1]] = {}
        for j in range (1,6):
            Dict[str(year)][teamList[i+1]][atrib[j]] = teamList[j+i+2]
        for j in range (4,6):
            Dict6[str(year)][teamList[i+1]][atrib[j]] = teamList[j+i+2]
        Dict5[str(year)][teamList[i+1]][atrib2[6]] = teamList[i+18]
        Dict[str(year)][teamList[i+1]][atrib2[7]] = teamList[i]
        Dict[str(year)][teamList[i+1]][atrib[7]] = AvgF[i/20]
        Dict[str(year)][teamList[i+1]][atrib[8]] = AvgA[i/20]
        Dict[str(year)][teamList[i+1]][atrib[9]] = AvgW[i/20]
        Dict3[str(year)][teamList[i+1]][atrib2[0]] = AvgFH[i/20]
        Dict2[str(year)][teamList[i+1]][atrib2[1]] = AvgAH[i/20]
        Dict4[str(year)][teamList[i+1]][atrib2[4]] = AvgWH[i/20]
        Dict3[str(year)][teamList[i+1]][atrib2[2]] = AvgFA[i/20]
        Dict2[str(year)][teamList[i+1]][atrib2[3]] = AvgAA[i/20]
        Dict4[str(year)][teamList[i+1]][atrib2[5]] = AvgWA[i/20]
        i += 20
    Dict[str(year)][atrib[10]] = total
    Dict[str(year)][atrib[11]] = Htotal
    Dict[str(year)][atrib[12]] = Atotal
    return Dict,Dict2,Dict3,Dict4,Dict5,Dict6,Dict7,Dict8,Dict9,Dict10,Dict11
            
def clear():
    del teamList[:]
    del AvgW[:]
    del AvgF[:]
    del AvgA[:]
    del AvgWH[:]
    del AvgFH[:]
    del AvgAH[:]
    del AvgWA[:]
    del AvgFA[:]
    del AvgAA[:]
    global total
    global Htotal
    global Atotal
    total = 0
    Htotal = 0
    Atotal = 0
    
if __name__ == '__main__':
    for year in range (2002,2013):
        url = 'http://espnfc.com/tables/_/league/eng.1/season/'+str(year)+'/barclays-premier-league'
        leagueTable(url)
        getAvgs(teamList)
        Totals(teamList)
        Sprint()
        AllDict(teamList2,teamList,AvgW,AvgWH,AvgWA,AvgF,AvgFH,AvgFA,AvgA,AvgAH,AvgAA,total,Htotal,Atotal,year)
        clear()
    #print simplejson.dumps(Dict, sort_keys = True, indent = 4)
    #with open('2002 to 2012 Home Goals Scored of Top Team.json', mode = 'w') as f:
    #    json.dump(Dict11,f,indent = 4)
    #with open('Home and Away Goals Conceded per Game per Season.json', mode = 'w') as f:
    #    json.dump(Dict2,f,indent = 4)
    #with open('Home and Away Goals Scored per Game per Season.json', mode = 'w') as f:
    #    json.dump(Dict3,f,indent = 4)
    #with open('Home and Away Win% per Team per Season.json', mode = 'w') as f:
    #    json.dump(Dict4,f,indent = 4)
    #with open('Goal Different.json', mode = 'w') as f:
    #    json.dump(Dict5,f,indent = 4)
    #with open('Goals Scored and Goals Conceded per Team per Season.json', mode = 'w') as f:
    #    json.dump(Dict6,f,indent = 4)
