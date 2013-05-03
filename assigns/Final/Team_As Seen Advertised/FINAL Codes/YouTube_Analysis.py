# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:48:16 2013

@author: Tank
"""
import urllib2
from BeautifulSoup import *
import re

fw = open("C:\\Users\\Tank\\Documents\\School\\FINAL660\\python_code\\youtubecomments.txt","w")
for i in range(4):    
    url='http://www.youtube.com/all_comments?v=S2nBBMbjS8w&page='+str(i)
#url was changed for each advertisementto capture YouTube comments
    search = urllib2.urlopen(url)
    html = search.read()
    soup = BeautifulSoup(html)
    for i in soup.findAll('div',{"class":"comment-text","dir":"ltr"}):#The body loop
        print i.text.encode("utf-8")
        fw.write(i.text.encode("utf-8")+'\n')
print len(soup.findAll('div',{"class":"comment-text","dir":"ltr"}))    
fw.close()  
