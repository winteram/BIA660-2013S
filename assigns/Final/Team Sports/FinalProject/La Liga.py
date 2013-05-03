import urllib2
import json
from BeautifulSoup import BeautifulSoup

allseasons=["2002-03","2003-04","2004-05","2005-06","2006-07","2007-08","2008-09","2009-10","2010-11","2011-12","2012-13"]
seasons=["2003-04","2004-05","2005-06","2006-07","2007-08","2008-09","2009-10","2010-11","2011-12","2012-13"] 

def openurl(url):
    page=urllib2.urlopen(url)
    page_txt=page.read()
    bstext=BeautifulSoup(page_txt)
    return bstext

#this function is to get the url
def geturl(bstext):
    opts=bstext.findAll("option")   
    url={}
    for opt in opts:
        for season in seasons:
            if opt.text==season:
                url[season]=opt["value"]
    return url

#this function is to get data from the table and return a dictionary that stores the data        
def getdata(bstext):
    one_season_data={}
    findtr=bstext.findAll("tr")
    for i in range(3,23):
        findtd=findtr[i].findAll("td")
        one_season_data[findtd[0].text]={"TEAM":"","OVERALL":{"Games Played":"","Win":"","Draw":"","Loss":"","Goals Scored":"","Goals Against":""},
                                         "HOME":{"Win":"","Draw":"","Loss":"","Goals Scored":"","Goals Against":""},
                                         "AWAY":{"Win":"","Draw":"","Loss":"","Goals Scored":"","Goals Against":""},"Goal Difference":"",
                                         "Points":""}
        
        one_season_data[findtd[0].text]["TEAM"]=findtd[2].text
        stat=["Games Played","Win","Draw","Loss","Goals Scored","Goals Against"]
        for i in range(6):
            one_season_data[findtd[0].text]["OVERALL"][stat[i]]=findtd[3+i].text
        for i in range(5):
            one_season_data[findtd[0].text]["HOME"][stat[i+1]]=findtd[10+i].text
            one_season_data[findtd[0].text]["AWAY"][stat[i+1]]=findtd[16+i].text
        one_season_data[findtd[0].text]["Goal Difference"]=findtd[22].text
        one_season_data[findtd[0].text]["Points"]=findtd[23].text
    return one_season_data

#this function is to output the sum of goals every season
def goals_sum(all_seasons_data):   
    all_goals_sum={}
    for season in allseasons:
        total_goals=0
        away_goals=0
        home_goals=0
        for i in range(1,21):
            total_goals +=int(all_seasons_data[season]['%d' % i]["OVERALL"]["Goals Scored"])
            home_goals +=int(all_seasons_data[season]['%d' % i]["HOME"]["Goals Scored"])
            away_goals +=int(all_seasons_data[season]['%d' % i]["AWAY"]["Goals Scored"])
        all_goals_sum[season]={}
        all_goals_sum[season]["TGS"]=total_goals
        all_goals_sum[season]["HGS"]=home_goals
        all_goals_sum[season]["AGS"]=away_goals
    fp=open("goals_sum.json","w")
    fp.write(json.dumps(all_goals_sum,indent=2))
    fp.close()

#this function is to output the rate of goals against and goals scored every team every season
#and goal difference, goals scored, goals against
def outputdata(all_seasons_data):
    seasons_rate_against={}
    seasons_rate_scored={}
    seasons_goal_dif={}
    seasons_goal_sco_again={}
    for season in allseasons:
        all_rate_against={}
        all_rate_scored={}
        goal_dif={}
        goal_sco_again={}
        for i in range(1,21):
            all_rate_against[all_seasons_data[season]['%d' % i]["TEAM"]]={}
            all_rate_scored[all_seasons_data[season]['%d' % i]["TEAM"]]={}
            goal_sco_again[all_seasons_data[season]['%d' % i]["TEAM"]]={}
            home_gameplayed=float(all_seasons_data[season]['%d' % i]["HOME"]["Win"])+float(all_seasons_data[season]['%d' % i]["HOME"]["Draw"])+float(all_seasons_data[season]['%d' % i]["HOME"]["Loss"])
            away_gameplayed=float(all_seasons_data[season]['%d' % i]["AWAY"]["Win"])+float(all_seasons_data[season]['%d' % i]["AWAY"]["Draw"])+float(all_seasons_data[season]['%d' % i]["AWAY"]["Loss"])
            home_scored=float(all_seasons_data[season]['%d' % i]["HOME"]["Goals Scored"])
            away_scored=float(all_seasons_data[season]['%d' % i]["AWAY"]["Goals Scored"])
            home_against=float(all_seasons_data[season]['%d' % i]["HOME"]["Goals Against"])
            away_against=float(all_seasons_data[season]['%d' % i]["AWAY"]["Goals Against"])
            all_rate_scored[all_seasons_data[season]['%d' % i]["TEAM"]]["HGSpG"]=home_scored/home_gameplayed
            all_rate_scored[all_seasons_data[season]['%d' % i]["TEAM"]]["AGSpG"]=away_scored/away_gameplayed
            all_rate_against[all_seasons_data[season]['%d' % i]["TEAM"]]["HGCpG"]=home_against/home_gameplayed
            all_rate_against[all_seasons_data[season]['%d' % i]["TEAM"]]["AGCpG"]=away_against/away_gameplayed
            goal_dif[all_seasons_data[season]['%d' % i]["TEAM"]]=int(all_seasons_data[season]['%d' % i]["Goal Difference"])
            goal_sco_again[all_seasons_data[season]['%d' % i]["TEAM"]]["GS"]=int(all_seasons_data[season]['%d' % i]["OVERALL"]["Goals Scored"])
            goal_sco_again[all_seasons_data[season]['%d' % i]["TEAM"]]["GC"]=int(all_seasons_data[season]['%d' % i]["OVERALL"]["Goals Against"])
        seasons_rate_against[season]=all_rate_against
        seasons_rate_scored[season]=all_rate_scored
        seasons_goal_dif[season]=goal_dif
        seasons_goal_sco_again[season]=goal_sco_again
    fp_against=open("rate_against.json","w")
    fp_scored=open("rate_scored.json","w")
    fp_goal_dif=open("goal_difference.json","w")
    fp_goal_sco_again=open("goal_scored_against.json","w")
    fp_against.write(json.dumps(seasons_rate_against,indent=2))
    fp_scored.write(json.dumps(seasons_rate_scored,indent=2))
    fp_goal_dif.write(json.dumps(seasons_goal_dif,indent=2))
    fp_goal_sco_again.write(json.dumps(seasons_goal_sco_again,indent=2))
    fp_against.close()
    fp_scored.close()
    fp_goal_dif.close()
    fp_goal_sco_again.close()


#this function is to get the rate of win each season each team
def rate_win(all_seasons_data):
    all_rate_win={}
    #initialize
    for season in allseasons:       
        for i in range(1,21):
            all_rate_win[all_seasons_data[season]['%d' % i]["TEAM"]]={}

    for season in allseasons:    
        for i in range(1,21):
            all_rate_win[all_seasons_data[season]['%d' % i]["TEAM"]][season]={}
            home_gameplayed=float(all_seasons_data[season]['%d' % i]["HOME"]["Win"])+float(all_seasons_data[season]['%d' % i]["HOME"]["Draw"])+float(all_seasons_data[season]['%d' % i]["HOME"]["Loss"])
            away_gameplayed=float(all_seasons_data[season]['%d' % i]["AWAY"]["Win"])+float(all_seasons_data[season]['%d' % i]["AWAY"]["Draw"])+float(all_seasons_data[season]['%d' % i]["AWAY"]["Loss"])
            home_win=float(all_seasons_data[season]['%d' % i]["HOME"]["Win"])
            away_win=float(all_seasons_data[season]['%d' % i]["AWAY"]["Win"])
            home_rate_win=home_win/home_gameplayed
            away_rate_win=away_win/away_gameplayed
            all_rate_win[all_seasons_data[season]['%d' % i]["TEAM"]][season]["HW%"]=home_rate_win
            all_rate_win[all_seasons_data[season]['%d' % i]["TEAM"]][season]["AW%"]=away_rate_win
    fp=open("rate_win.json","w")
    fp.write(json.dumps(all_rate_win,indent=2))
    fp.close()
            


if __name__=="__main__":
    all_seasons_data={}
    first_url="http://espnfc.com/tables/_/league/esp.1/season/2002/spanish-primera-division?cc=5901"
    bstext=openurl(first_url)
    all_seasons_data["2002-03"]=getdata(bstext)
    '''get other seasons' data'''
    url=geturl(bstext)
    for season in seasons:
        bstext=openurl(url[season])
        all_seasons_data[season]=getdata(bstext)
    goals_sum(all_seasons_data)
    outputdata(all_seasons_data)
    rate_win(all_seasons_data)

    
