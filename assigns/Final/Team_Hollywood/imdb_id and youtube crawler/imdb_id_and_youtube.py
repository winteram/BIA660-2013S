import urllib2
from BeautifulSoup import BeautifulSoup
import re
import json

#not actually used in the end, because we decide to get ids from producer pages after a disscussion
# it can get all the film ids in a page like "http://www.imdb.com/search/title?at=0&countries=us&sort=moviemeter,asc&title_type=feature&year=2012,2012"
def find_imdb_filmid(url):
#url ="http://www.imdb.com/search/title?at=0&countries=us&sort=moviemeter,asc&title_type=feature&year=2012,2012"
	source = urllib2.urlopen(url)   # open the url
	soup = BeautifulSoup(source.read())
	films = soup.findAll((lambda tag: len(tag.attrs) == 4),attrs={'data-tconst' : re.compile("tt*")})   #find the tags that have 4 attributes and one of the attribute names data-tconst
	for film_info in films:
		id = film_info['data-tconst']  #get the data-tconst's content
		#print id
		
#not actually used in the end, because we decide to get ids from producer pages after a disscussion
# it can get the total film numer of the search result page like "http://www.imdb.com/search/title?at=0&countries=us&sort=moviemeter,asc&title_type=feature&year=2012,2012"
def find_total(url):
#url ="http://www.imdb.com/search/title?at=0&countries=us&sort=moviemeter,asc&title_type=feature&year=2012,2012"
	total = soup.find(id="left")
	t_num = re.split(" ",str(total.contents))
	num = re.split('n',t_num[2])
	return int(num[0][:len(num[0])-1].replace(',',''))

# get film ids according to the producer list, min_year and max_year are used to control the films released years
def get_filmid_by_producer(producers,min_year,max_year):
#url = "http://www.imdb.com/company/co0023400/"
	f = open("ids.txt", 'w')
	for key in producers.keys():
		count =0
		producer_url = "http://www.imdb.com/company/"+producers[key]
		source = urllib2.urlopen(producer_url)   
		soup = BeautifulSoup(source.read())  
		lists = soup.findAll('li')
		#lists = soup.html.body.ol.findAll()
		for i in lists:
			if(len(i.contents)==3 and (i.contents[2].string.find("Production Company")!=-1) and ( i.contents[1].string.split()[0][1:5]!= "????")):	
				if (int(i.contents[1].string.split()[0][1:5]) >= min_year and int(i.contents[1].string.split()[0][1:5])<= max_year):
					if( i.contents[0].contents[0].find("The Making of") ==-1 and i.contents[0].contents[0].find("(")==-1):
						count += 1
						print "processing "+i.contents[0]['href'].split("/")[2]+" "+ str(i.contents[0].contents).replace('&#x27;',"'").replace("&#x22;",'"').replace("&#x26;","&")[3:-2]
						# write: counter, film_id, producer, release_year, (film_name) to the file, a line for each film
						f.write("%d %s %s %d (%s)\n"%(count,i.contents[0]['href'].split("/")[2],key,int(i.contents[1].string.split()[0][1:5]),str(i.contents[0].contents).replace('&#x27;',"'").replace("&#x22;",'"').replace("&#x26;","&")[3:-2]))


# find likes number in the input url (youtube)
def find_like(url):
	source = urllib2.urlopen(url) 
	soup = BeautifulSoup(source.read()) 
	films = soup.findAll('span',attrs={'class' : "likes-count"})
	if films:
		if len(str(films[0].contents).replace(',',''))>4:
			return int(str(films[0].contents).replace(',','')[3:-2])
		else:
			return 0
	else:
		return 0

# find	dislikes number in the input url (youtube)
def find_dislike(url):
	source = urllib2.urlopen(url) 
	soup = BeautifulSoup(source.read()) 
	films = soup.findAll('span',attrs={'class' : "dislikes-count"})
	if films:
		if len(str(films[0].contents).replace(',',''))>4:
			return int(str(films[0].contents).replace(',','')[3:-2])
		else:
			return 0
	else:
		return 0

# find	trailer views number for a film (use film name) (youtube)
# It may get several videos for each film, the function will get all the views on the result page, and record the max number as the final result
# Meanwhile it will record the video link which has the max views, and go into that url and find likes and dislikes number
def find_trailer_views(film_name,f,filmid):
	query = film_name.replace(' ','+')
	view_num_dict = {}
	url =  "https://www.youtube.com/results?search_query="+query+"+trailer"
	source = urllib2.urlopen(url) 
	soup = BeautifulSoup(source.read())  
	views = soup.html.findAll('li',attrs = {'data-context-item-views': re.compile("views$")})
	# find the max views in the result page
	for i in views:
		if (("%s"%i['data-context-item-title']).upper().find(film_name.upper())!=-1):
			#print str(i['data-context-item-title'])+" "+str(i['data-context-item-views'])+"\n"
			if "%s"%i['data-context-item-views'] != "No views":
				view_num_dict[int(("%s"%i['data-context-item-views']).split()[0].replace(',',''))] = ("%s"%i['data-context-item-views']).split()[0]
			else:
				view_num_dict[0] = 0
	# go to the max views video link and find likes and dislike number, write them to the "views.txt"
	if view_num_dict:
		view_num_dict = sorted(view_num_dict.items(), key=lambda view_num_dict:view_num_dict[0])
		if view_num_dict[-1][0]!=0:
			res1= soup.html.findAll('li',attrs = {'data-context-item-views': re.compile(view_num_dict[-1][1])})
			url2 = "https://www.youtube.com"+ res1[0].contents[1].contents[1]['href']
			print url2
			likes = find_like(url2)
			dislikes = find_dislike(url2)
			print film_name+" %d"%view_num_dict[-1][0]+" %d "%likes+" %d "%dislikes
			f.write("%s %s (%d) (%d) (%d)\n"%(filmid,film_name,view_num_dict[-1][0],likes,dislikes))
		else:
			print film_name+" %d"%0+" %d"%0+" %d "%0
			f.write("%s %s (%d) (%d) (%d)\n"%(filmid,film_name,0,0,0))
		return view_num_dict[-1][0]
	else:
		print film_name+" %d"%0+" %d"%0+" %d "%0
		f.write("%s %s (%d) (%d) (%d)\n"%(filmid,film_name,0,0,0))
		return 0

# get all the film names and get the views, likes and dislikes number
def find_films_trailer_views(film_name_dict):
	f = open("views.txt", 'w')
	for name in film_name_dict:
		for k,v in name.items():
			trailer_views = find_trailer_views(v,f,k)
						

# could be used to generate a json file,used in generate_d3_json()
# not actually used in the end
def get_all_values(a_list,key):
	v_list=[]
	for element in a_list:
		if element[key] not in v_list:
			v_list.append(element[key])
	return v_list
	
# could be used to generate a json file, used in generate_d3_json()
# not actually used in the end
def add_index(value_list):
	counter =0
	lis =[]
	for i in value_list:
		di ={}
		di[i]=counter
		lis.append(di)
		counter +=1
	for i in range(0,len(lis)):
		lis[i] = {v:k for k, v in lis[i].items()}
	return lis

# could be used to generate a json file, used in generate_d3_json()
# not actually used in the end
def find_list_entrance(avalue,list1):
	index=0
	for i in range (0, len(list1)):
		if (list1[i].values()[0] == avalue):
			index = i
			break
	return index

	
# generate a json file that can be used to generate a d3 Tree graph directly
# graph example link: http://bl.ocks.org/mbostock/4063550
def generate_d3_json():
	f = open("ids.txt", 'r')
	file1 = f.readlines()
	d =[]
	for line in file1:
		di ={}
		di['company'] = line.split()[2]
		di['name'] = line.split('(')[1][:-2]
		d.append(di)
	value_list = get_all_values(d,'company')
	value_list = add_index(value_list)
	li = []
	di={}
	di['name']='producer'
	di['children']=[]
	li.append(di)
	for v in value_list:
		di={}
		di['name']="%s"%v.values()[0]
		di['children']=[]
		li[0]['children'].append(di)
	for e in d:
		ind =find_list_entrance(e['company'],value_list)
		di={}
		di['name']=e['name']
		li[0]['children'][ind]['children'].append(di)
	j =	json.dumps(li, indent=4)
	f = open("names.json", 'w')
	f.write(j)	
	
if __name__ == "__main__":
	
	# will get all the films produced by the following 6 producers
	producers = {'columbia':'co0050868',"paramount_pic":"co0023400","walt_Disney":"co0008970","MGM":"co0016037","universal":"co0005073","Warner_Bros":"co0026840"}	
	# call the 	get_filmid_by_producer to get all the film ids and write them into a "ids.txt" in our project we choose to use the films released between 1990 and 2012
	get_filmid_by_producer(producers,1990,2012)
	
	
	# after ids.txt is generated, get film names from that, and use them to find all film views, dislikes, likes number from youtube, may take a while to get all the data, it has to go through thousands of urls
	# will write the result to views.txt
	# f = open("ids.txt", 'r')
	# file1 = f.readlines()
	# d =[]
	# for line in file1:
	# 	di={}
	# 	di[line.split()[1]] =line.split('(')[1][:-2]
	# 	d.append(di)
	# find_films_trailer_views(d)

	
	# generate a json file that can be used to generate a d3 Tree graph directly
	# graph example link: http://bl.ocks.org/mbostock/4063550
	# not actually used in the end because its kind of ugly...
	# generate_d3_json()





