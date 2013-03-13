'''
Created on Mar 2, 2013

@author: zbl
'''
import urllib2
from bs4 import BeautifulSoup
import re
import xlwt

#def query(page, CataNum, proName, row, sheet):
def query(page, proName, proId, row, sheet):    
    
    unire = re.compile("[\w\s()*&%$@/!~<>.,?`~]")
    datere = re.compile("[0-9()*&%$@/!~<>.,?`~]")
    title_list = list(range(0))
    rate_list = list(range(0))
    reco_list = list(range(0))
    review_list = list(range(0))
    date_list = list(range(0))
    name_list = list(range(0))
    #myfile = open("tesco_kindle_"+CataNum+".txt","w")
    for i in range (1, page+1):
        #search = urllib2.urlopen("http://topsy.com/s/"+term+"/tweet?&om=b&window=h&offset="+str(i*10)+"&page="+str(i))
        search = urllib2.urlopen("http://www.ebay.com/rvw/"+proName+"-/"+proId+"?rt=nc&_dmpt=US_Tablets&_pcategid=171485&_pcatid=839&_trksid=p5797.c0.m1724&_pgn="+str(i))
                                 # http://www.ebay.com/rvw/Amazon-Kindle-2GB-Wi-Fi-6in-Graphite-/111337530?rt=nc&_dmpt=US_Tablets&_pcategid=171485&_pcatid=839&_trksid=p5797.c0.m1724&_pgn=2
        #search = urllib2.urlopen("http://www.bestbuy.com/site/searchpage.jsp?_dyncharset=ISO-8859-1&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=15&sp=&qp=&list=n&iht=y&usc=All+Categories&ks=960&st=kindle")
        html = search.read()
        soup = BeautifulSoup(html)
        
        #print soup
        print "page"+str(i)
        for body in soup.findAll('h2', {'itemprop': 'name'}):
            body = ''.join(unire.findall(body.text))
            title_list.append(body)
            print body
        print ""
        #print "a begin"
        for body in soup.findAll('span',{'itemprop': 'reviewRating'} ):
            #body = ''.join(unire.findall(body.get('title').text))
            rate_list.append(body.get('content'))
            print body.get('content')
        print ""
        for body in soup.findAll('div',class_="rvp-rec" ):
            #body = ''.join(unire.findall(body.get('title').text))
            body = ''.join(unire.findall(body.text))
            reco_list.append(body)
            print body
        for body in soup.findAll('div',{'itemprop': 'reviewBody'} ):
            #body = ''.join(unire.findall(body.get('title').text))
            body = ''.join(unire.findall(body.text))
            review_list.append(body)
            print body
        for body in soup.findAll('span', class_="rvp-cd rvp-r"):
            body = ''.join(datere.findall(body.text))
            date_list.append(body)
            print body
        for body in soup.findAll('div', class_="ds3mb"):
            #body = ''.join(datere.findall(body.a.text))
            name_list.append(body.a.string)
            print body.a.string
            
        print ""
        print ""
        
    print "title: "+str(len(title_list))
    print "rate: "+str(len(rate_list))
    print "reco: "+str(len(reco_list))
    print "review: "+str(len(review_list))
    print "date: "+str(len(date_list))
    print "name: "+str(len(name_list))
    
    for i in range(0, len(title_list), 1):
        sheet.write(row,0,proId)
        sheet.write(row,1,'eBay')
        sheet.write(row,2,proName)
        sheet.write(row,3,name_list[i])
        sheet.write(row,4,reco_list[i])
        sheet.write(row,5,date_list[i])
        sheet.write(row,6,title_list[i])
        sheet.write(row,7,review_list[i])
        sheet.write(row,8,'ebay.com')
        row+=1
            #for body1 in body.h2.findAll(itemprop_="name"):
                #body1 = ''.join(unire.findall(body1.text))
                #print body1
    return row        

if __name__ == "__main__":
    wbk=xlwt.Workbook()

    sheet=wbk.add_sheet('sheet 1')

    sheet.write(0,0,'Product ID')
    sheet.write(0,1,'Brand')
    sheet.write(0,2,'Model Description')
    sheet.write(0,3,'Reviewer')
    sheet.write(0,4,'Rocommendation')
    sheet.write(0,5,'Review Date')
    sheet.write(0,6,'Review Title')
    sheet.write(0,7,'Comments')
    sheet.write(0,8,'Review Source')  
    row = 1  
    row = query(2, "Amazon-Kindle-6-E-Ink-Display-2GB-Wi-Fi-6in-Black-Latest-Model", "128678074", row , sheet)
    row = query(4, "Amazon-Kindle-2GB-Wi-Fi-6in-Graphite","111337530", row , sheet)
    row = query(13, "Amazon-Kindle-6-E-Ink-Display-2GB-Wi-Fi-6in-Graphite", "110808283", row , sheet)
    row = query(21, "Amazon-Kindle-Touch-4GB-Wi-Fi-6in-Silver", "110778468", row , sheet)
    row = query(13, "Amazon-Kindle-6-E-Ink-Display-2GB-Wi-Fi-6in-Graphite", "110808283", row , sheet)
    row = query(4, "Amazon-Kindle-2GB-Wi-Fi-6in-Graphite", "111337530", row , sheet)
    row = query(57, "Amazon-Kindle-Fire-8GB-Wi-Fi-7in-Black-New-Edition-Latest-Model", "110592598", row , sheet)
    row = query(2, "Amazon-Kindle-Paperwhite-2GB-Wi-Fi-6in-Black-Latest-Model", "127462501", row , sheet)
    
    row = query(30, "Amazon-Kindle-Keyboard-4GB-Wi-Fi-6in-Graphite", "108970839", row , sheet)
    row = query(2, "Amazon-Kindle-Fire-8GB-Wi-Fi-7in-Black", "135706466", row , sheet)
    row = query(4, "Amazon-Kindle-Touch-4GB-Wi-Fi-3G-Unlocked-6in-Silver", "110723062", row , sheet)
    row = query(18, "Amazon-Kindle-Keyboard-4GB-Wi-Fi-3G-Unlocked-6in-White", "103128196", row , sheet)
    row = query(1, "Amazon-Kindle-Keyboard-4GB-Wi-Fi-3G-6in-Graphite", "115269136", row , sheet)
    row = query(10, "Amazon-Kindle-DX-4GB-3G-Unlocked-9-7in-Graphite", "108359554", row , sheet)
    row = query(20, "Amazon-Kindle-2-2GB-Wi-Fi-3G-Unlocked-6in-White", "103114312", row , sheet)
    row = query(7, "Amazon-Kindle-Fire-HD-16GB-Wi-Fi-7in-Black-Latest-Model", "127573348", row , sheet)
    row = query(18, "Amazon-Kindle-Keyboard-4GB-Wi-Fi-3G-Unlocked-6in-Graphite", "103128286", row , sheet)
    row = query(1, "Amazon-Kindle-Touch-4GB-Wi-Fi-3G-AT-T-6in-Silver", "111306069", row , sheet)
    row = query(7, "Amazon-Kindle-Touch-4GB-Wi-Fi-6in-Silver", "110778508", row , sheet)
    wbk.save("eBayKindle.xls")
    #query(, "", "")
    #query(, "", "")
    