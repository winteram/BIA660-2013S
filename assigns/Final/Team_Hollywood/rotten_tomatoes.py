import urllib2
import simplejson
import json
import re

def getWebValues(movie_id,output):
        # Get critics and audience comments, ratings and scores from rotten tomatoes for a movie based on the unique identifier from the IMDB site
        apikey = "wyk59zhwmxfq85u3eg4u2ett"
        url = "http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json?type=imdb&id=%s&apikey=%s&_prettyprint=true" %(movie_id,apikey)

        #Read data from the webpage       
        source = urllib2.urlopen(url)
        json_object = source.read()

        response_dict = json.loads(json_object)

        #Initialization 
        result = []
       # cc_dict = {}
        rating_dict = {}

        #Check if URL for the given movie id exists
        #If URL is not present, continue
        if response_dict.has_key('error'):
                pass
        #If URL exists, then retrieve the movie information
        else:
                ## Extracting critics consensus
                #if response_dict.has_key('critics_consensus'):
                #        cc_dict ['critics_consensus'] = response_dict['critics_consensus']
                #        result.append(cc_dict)
                #Extracting crticts ratings and scores followed by audience ratings and scores
                if response_dict.has_key('ratings'):
                        
                        ##Check if movie is rated by the critics
                        #if response_dict.get("ratings",{}).has_key('critics_rating'):
                        #        rating_dict['critics_rating'] = response_dict.get("ratings",{}).get("critics_rating")
                                
                        #Check if movie is given scores by the critics
                        if response_dict.get("ratings",{}).has_key('critics_score'):
                                rating_dict['critics_score'] = response_dict.get("ratings",{}).get("critics_score")
                                
                        ##Check if movie is rated by the audience
                        #if response_dict.get("ratings",{}).has_key('audience_rating'):
                        #        rating_dict['audience_rating'] = response_dict.get("ratings",{}).get("audience_rating")
                                
                        #Check if movie is given scores by the audience
                        if response_dict.get("ratings",{}).has_key('audience_score'):
                                rating_dict['audience_score'] = response_dict.get("ratings",{}).get("audience_score")
               
                        result.append(rating_dict)

                #Write the extracted movie information to output file
                output.write(''.join(('tt',movie_id)))
                for data in result:
                    output.write(" %s " %data)
                output.write('\n')

if __name__ == "__main__":

        #source = urllib2.urlopen('http://localhost:8080/txt/ids.txt')
        
        #Read all the movie identifiers retrieved from IMDB site
        source = open('C:/1 Stevens/Web_Analytics/Project/Test/ids.txt','r')
        movies = source.readlines()
        output = open('C:/1 Stevens/Web_Analytics/Project/Test/output.txt','w')
        #Get information for each movie belonging to a particular production company 
        for line in movies:
                movie_id = str(line.split()[1])[2:9]
                #Function to get movie information
                getWebValues(movie_id,output)
        source.close()
        output.close()	
