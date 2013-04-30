import pandas
import re

sb_fpositive=open('posi.txt','r')
sb_positive=[line.strip() for line in sb_fpositive]
sb_fnegative=open('neg.txt','r')
sb_negative=[line.strip() for line in sb_fnegative]

tv_fpositive=open('posi.txt','r')
tv_positive=[line.strip() for line in tv_fpositive]
tv_fnegative=open('neg.txt','r')
tv_negative=[line.strip() for line in tv_fnegative]

v_fpositive=open('posi.txt','r')
v_positive=[line.strip() for line in v_fpositive]
v_fnegative=open('neg.txt','r')
v_negative=[line.strip() for line in v_fnegative]

coca=open('YouTube_Clean_cocacola.txt','r')
doritos=open('YouTube_Clean_doritos.txt','r')
etrade=open('YouTube_Clean_etrade.txt','r')
godaddy=open('YouTube_Clean_godaddy.txt','r')

microsoft=open('YouTube_Clean_microsoft.txt','r')
nestle=open('YouTube_Clean_nestle.txt','r')
ikea=open('YouTube_Clean_ikea.txt','r')

evian=open('YouTube_Clean_evian.txt','r')
oldspice=open('YouTube_Clean_oldspice.txt','r')
blend=open('YouTube_Clean_will it blend.txt','r')


filename=[coca,doritos,etrade,godaddy,microsoft,nestle,ikea,evian,oldspice,blend]

productname=['Coca Cola','Doritos','Etrade','Godaddy','Microsoft','Nestle','IKEA','Evian','Oldspice','Will It Blend']

outputfile=open('frame2.txt','w')

def creat_dict(filename,phone,positive,negative):
    dictionary={}
    dictionary['1.Product']=phone
    dictionary['2.Positive']=0
    dictionary['3.Negative']=0
    dictionary['5.Tweets_Count']=0
    line=filename.readline()
    while line:
        for p in positive:
            ret=re.findall(p,line)
            if ret:
                dictionary['2.Positive'] +=len(ret)
        for p in negative:
            ret=re.findall(p,line)
            if ret:
                dictionary['3.Negative'] +=len(ret)
        dictionary['5.Tweets_Count'] +=1
        line=filename.readline()
        while line=='\n':
            line=filename.readline()
    dictionary['4.Positive percentage']='%.2f%%' % ((float (dictionary['2.Positive']*100))/(float (dictionary['2.Positive']+dictionary['3.Negative'])))
    return dictionary

sb_frame=[]
tv_frame=[]
v_frame=[]
for i in range(0,4):
    dictionary=creat_dict(filename[i],productname[i],sb_positive,sb_negative)
    sb_frame.append(dictionary)
for i in range(4,7):
    dictionary=creat_dict(filename[i],productname[i],tv_positive,tv_negative)
    tv_frame.append(dictionary)
for i in range(7,10):
    dictionary=creat_dict(filename[i],productname[i],v_positive,v_negative)
    v_frame.append(dictionary)
sb_df=pandas.DataFrame(sb_frame)
tv_df=pandas.DataFrame(tv_frame)
v_df=pandas.DataFrame(v_frame)

stroutput='%s\n\n\n' % sb_df
outputfile.write(stroutput)
stroutput='%s' % tv_df
outputfile.write(stroutput)
stroutput='%s' % v_df
outputfile.write(stroutput)
print sb_df
print '\n\n\n'
print tv_df
print '\n\n\n'
print v_df
sb_fpositive.close()
sb_fnegative.close()
tv_fpositive.close()
tv_fnegative.close()
v_fpositive.close()
v_fnegative.close()
outputfile.close()
for f in filename:
    f.close()    

