def AmazonSoup():
  from bs4 import BeautifulSoup
  import urllib2
  import re
  from datetime import datetime as DT
  import MySQLdb as db

  conn = db.connect(user="procyk01",  passwd="helios21", host="mysql11.brinkster.com", db="procyk01")
  cur = conn.cursor()

  regedTweet = re.compile("[\w\s()*&%$@!~<>.]")
  
  ReviewSource = "Amazon.com"  
  SourceID = 1

  #ReviewSource = "BestBuy.com"  
  #SourceID = 2  

  #iStart = 201
  #iFinish = 251
  #Brand = "Amazon"
  #Model = "Kindle"
  #ModelID = "B007HCCNJU"
  #ModelDescr = "Kindle-Ereader-ebook-reader"
  #ModelName =  "Kindle Ereader"
  ## note - approx 2781 reviews
  ## left off at iFinish = 251 pages
  
  #iStart = 601
  #iFinish = 651
  #Brand = "Amazon"
  #Model = "Kindle"
  #ModelID = "B007OZNUCE"
  #ModelDescr = "Kindle-Paperwhite-3G"
  #ModelName =  "Kindle Paperwhite 3G"
  ### note - approx 6993 reviews
  ### left off at iFinish = 651

  iStart = 501
  iFinish = 551
  Brand = "Amazon"
  Model = "Kindle"
  ModelID = "B004HZYA6E "
  ModelDescr = "Kindle-Keyboard-Free-Wi-Fi-Display"
  #ModelName =  "Kindle Keyboard 3G"
  ## note - approx 39457 reviews
  ## left off at iFinish =  501


  #iStart = 1
  #iFinish = 8
  #Brand = "Sony"  
  #Model = "eReader"
  #ModelID = "B005MIZKW8"
  #ModelDescr = "Sony-PRS-T1-Digital-E-Ink-eReader"
  #ModelName =  "Sony PRS T1"
  ## note - approx 69 reviews
  ## left off at iFinish =  8 (done)


  #iStart = 1
  #iFinish = 15
  #Brand = "Sony"  
  #Model = "eReader"
  #ModelID = "B002MSNS4S"
  #ModelDescr = "Sony-Reader-Pocket-Edition-PRS-300SC"
  #ModelName =  "Sony PRS 300"
  ## note - approx 138 reviews
  ## left off at iFinish =    15 (done)


  #iStart = 1
  #iFinish = 3
  #Brand = "Sony"  
  #Model = "eReader"
  #ModelID = "B008UNSPO2"
  #ModelDescr = "Sony-PRS-T2-Touchscreen-WiFi-eReader"
  #ModelName =  "Sony PRS 21"
  ## note - approx 13 reviews
  ## left off at iFinish =   3 (done)


  #iStart = 1
  #iFinish = 9
  #Brand = "Sony"  
  #Model = "eReader"
  #ModelID = "B002MSHQ46"
  #ModelDescr = "Sony-Digital-Reader-Touch-Edition"
  #ModelName =  "Sony Digital Reader Touch Edition"
  ## note - approx 70 reviews
  ## left off at iFinish =   9 (done)


  #iStart = 1
  #iFinish = 4
  #Brand = "Sony"  
  #Model = "eReader"
  #ModelID = "B005MIZKXM"
  #ModelDescr = "Sony-PRS-T1-Pearl-eBook-Reader"
  #ModelName =  "Sony PRS T1 Pearl eBook Reader"
  ## note - approx 16 reviews
  ## left off at iFinish = 4        (done)


  #iStart = 1
  #iFinish = 6
  #Brand = "Kobo"  
  #Model = "eReader Touch"
  #ModelID = "B0058NULKS"
  #ModelDescr = "Kobo-N905-KBO-B-eReader-Touch-Black"
  #ModelName =  "Kobo eReader Touch"
  ## note - approx 43 reviews
  ## left off at iFinish =  6       (done)


  #iStart = 1
  #iFinish = 3
  #Brand = "Kobo"  
  #Model = "eReader Glo"
  #ModelID = "B00AEFFLJQ"
  #ModelDescr = "Kobo-Glo-Ereader-Pearl-Screen"
  #ModelName =  "Kobo Glo eReader"
  ## note - approx 9 reviews
  ## left off at iFinish =  3    (done)


  #iStart = 1
  #iFinish = 8
  #Brand = "Kobo"  
  #Model = "eReader Wifi"
  #ModelID = "B003UE4A86"
  #ModelDescr = "Kobo-N289-BUS-B-Wifi-eReader"
  #ModelName =  "Kobo Wifi eReader"
  ## note - approx 66 reviews
  ## left off at iFinish =  8 (done)


  for iPg in range(iStart,iFinish,1):
    webPageLink = "http://www.amazon.com/" + ModelDescr + "/product-reviews/" + ModelID + "/ref=cm_cr_pr_btm_link_" + str(iPg) + "?ie=UTF8&pageNumber=" + str(iPg) + "&showViewpoints=0"
    #webPageLink = "http://www.amazon.com/Kindle-Ink-Display-Wi-Fi-Black/product-reviews/B007HCCOIA/ref=cm_cr_pr_btm_link_" + str(iPg) + "?ie=UTF8&pageNumber=" + str(iPg) + "&showViewpoints=0"
    #webPageLink = "http://www.amazon.com/Kindle-Ink-Display-Wi-Fi-Black/product-reviews/B007HCCOIA/ref=cm_cr_pr_btm_link_2?ie=UTF8&pageNumber=2&showViewpoints=0"

    webPage=urllib2.urlopen(webPageLink)
    webText = webPage.read()
    webSoup = BeautifulSoup(webText)

    strSQL = "INSERT INTO Reviews (IDModel, Reviewer, Rating, IDSource, ReviewTitle, ReviewDate) VALUES "
           
    blnHasParens = 0

    for i in range(5,-1,-1):
      for stars in webSoup.findAll("span",class_="swSprite s_star_" + str(i) + "_0 "):
        if stars == None:
          continue 
        else:
          findRating = stars.find_next("span").find_next("span")
          findMoreText = findRating.find_next("span")                      

          #if findMoreText[:9] == " Previous": 
          #  continue 
          #elif findMoreText[:18] == "2.0 out of 5 stars":         
          #  continue
          

          Rating = ''.join(regedTweet.findall(stars.string))[0]
          #Title = ''.join(regedTweet.findall(findRating.text))
          Reviewer= ''.join(regedTweet.findall(findMoreText.text))
          
          #if findRating.children[0].string == "2.0 out of 5 stars":  
          #  continue 
          #elif Title[:18] == "2.0 out of 5 stars":         
          #  continue

          if findRating.find('b') == None: continue

          Title = findRating.find('b').text
          RevDt = findRating.find('nobr').text     #''.join(regedTweet.findall("nobr").text)

          #Title = ''.join(regedTweet.findall(a.text))                                                       
          #Reviewer= ''.join(regedTweet.findall(b.text))

          #if Title[:9] == " Previous": 
          #  continue 
          #elif Title[:18] == "2.0 out of 5 stars":         
          #  continue
          #else:
          
          #print DT.strftime(DT.strptime(RevDt, "%B %d, %Y"),"%Y-%m-%d")

          #print "Rating: " + Rating, "Title: " + Title, "Reviewer: " + Reviewer, "RevDt: " + str(RevDt)
          #strSQL = "INSERT INTO Reviews (IDModel, Reviewer, Rating, IDSource, ReviewTitle, ReviewDate) VALUES "
          
          #if blnHasParens: strSQL += ","
          #strSQL += "(\'" + ModelID + "\',\'" + Reviewer + "\'," + str(Rating) + "," + str(SourceID) + ",\'" + Title + "\',\'" + DT.strftime(DT.strptime(RevDt, "%B %d, %Y"),"%Y-%m-%d") + "\')"
          try:
            strSQLFrag = "('" + ModelID + "','" + db.escape_string(Reviewer) + "'," + str(Rating) + "," + db.escape_string(str(SourceID)) + ",'" + db.escape_string(Title) + "','" + DT.strftime(DT.strptime(RevDt, "%B %d, %Y"),"%Y-%m-%d") + "')"
            #blnHasParens = 1
          except:
            print "error in row " + str(iPg)
          else:
            if blnHasParens: strSQL += ","
            strSQL += strSQLFrag
            blnHasParens = 1

    print iPg, strSQL
    cur.execute(strSQL)
                        



if __name__ == "__main__" :
  AmazonSoup()  
  #tryMysqlDBConnectionCursorsNetwork()
  print "DONE"
