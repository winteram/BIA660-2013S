import urllib2

from BeautifulSoup import BeautifulSoup

from mechanize import Browser

import re

 

def getunicode(soup):

	body=''

	if isinstance(soup, unicode):

		soup = soup.replace('&#39;',"'")

		soup = soup.replace('&quot;','"')

		soup = soup.replace('&nbsp;',' ')

		body = body + soup

	else:

		if not soup.contents:

			return ''

		con_list = soup.contents

		for con in con_list:

			body = body + getunicode(con)

	return body

 

 

def main(d,control):

	f = open("ids.txt", 'r')
	g=open("gross.txt","a")
        file1 = f.readlines()

        counter =0

        for line in file1:

                counter += 1

                if (counter <= control):

    

                        imdb_dict = {}
			

                        url='http://www.imdb.com/title/'+line.split()[1]+'/business?ref_=tt_dt_bus'

                        page=urllib2.urlopen(url)

                        soup=BeautifulSoup(page.read())

			
                        
                        
                        gross=soup.find('h4', attrs={"class" :"inline"}, text = 'Gross:')
                        gross=gross.next
      
 
				

                        imdb_dict ['id'] = str(line.split()[1])

			

			
			
                        imdb_dict ['gross'] = gross[8:22]
                       

			

                        d.append(imdb_dict)

			
			

                        g.write('[%s] [%s]   \n'%(imdb_dict ['id'],imdb_dict ['gross'] ))
        g.close 

	

    

if __name__ == '__main__':

        d=[]

        main(d,2510)


		
