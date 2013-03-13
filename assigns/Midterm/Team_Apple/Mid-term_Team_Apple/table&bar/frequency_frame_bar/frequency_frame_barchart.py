import pandas
import numpy as np
import matplotlib.pyplot as plt
import re

f1=open('D:\python_midterm\status\usertweets.txt','r')
f2=open('D:\python_midterm\status\usertweets2.txt','r')
f3=open('D:\python_midterm\status\usertweets3.txt','r')
f4=open('D:\python_midterm\status\usertweets4.txt','r')
f5=open('D:\python_midterm\status\usertweets5.txt','r')
f6=open('D:\python_midterm\status\usertweets6.txt','r')
filename=[f1,f2,f3,f4,f5,f6]

outputfile=open('frequency_bar.txt','w')

iphone=r'\b[^a-zA-Z]*[iI][pP][hH][oO][nN][eE][^a-zA-Z]*\b'
galaxy=r'\b[^a-zA-Z]*[gG][aA][lL][aA][xX][yY][^a-zA-Z]*\b'
lumia=r'\b[^a-zA-Z]*[lL][uU][mM][iI][aA][^a-zA-Z]*\b'
ios=r'\b[^a-zA-Z]*[iI][oO][sS][^a-zA-Z]*\b'
android=r'\b[^a-zA-Z]*[aA][nN][dD][rR][oO][iI][dD][^a-zA-Z]*\b'
windowsphone=r'\b[^a-zA-Z]*[wW][iI][nN][dD][oO][wW][sS][pP][hH][oO][nN][eE][^a-zA-Z]*\b'

keywords=[iphone,galaxy,lumia,ios,android,windowsphone]
pdctnm=['1.Iphone','2.Galaxy','3.Lumia','4.IOS','5.Android','6.Windowsphone']

frame=[{}]
for p in pdctnm:
    frame[0][p]=0
frame[0]['7.Total Tweets']=0

def creat_dict(filename):
    global frame
    global pdctnm
    global keywords
   
    line=filename.readline()
    while line:
        for p in range(0,6):
            ret=re.findall(keywords[p],line)
            if ret:
                frame[0][pdctnm[p]] +=len(ret)
        frame[0]['7.Total Tweets'] +=1
        line=filename.readline()

for i in range(0,6):
    creat_dict(filename[i])

df=pandas.DataFrame(frame)

print df
strdf='%s' % df
outputfile.write(strdf)
outputfile.close()
for f in filename:
    f.close()

                                    
#bar chart
plt.figure(figsize=(20,15))
ind=np.arange(6)
bar_data=[]
for i in range(0,6):
    bar_data.append(frame[0][pdctnm[i]])

plt.figure()
bar_chart=plt.bar(ind,bar_data,0.8,color='g')
plt.xlabel('Product Name')
plt.ylabel('The number of mentioning Tweets')
plt.title('Products'' Popularity')
plt.xticks(ind+0.4,(pdctnm))
plt.savefig('frequency_bar.png')
