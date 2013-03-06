import pandas
import re

ph_fpositive=open('phone_positive.txt','r')
ph_positive=[line.strip() for line in ph_fpositive]
ph_fnegative=open('phone_negative.txt','r')
ph_negative=[line.strip() for line in ph_fnegative]

sys_fpositive=open('system_positive.txt','r')
sys_positive=[line.strip() for line in sys_fpositive]
sys_fnegative=open('system_negative.txt','r')
sys_negative=[line.strip() for line in sys_fnegative]

iphone=open('iphone.txt','r')
samsung=open('samsung.txt','r')
lumia=open('lumia.txt','r')
ios=open('ios.txt','r')
android=open('android.txt','r')
windowsphone=open('windowsphone.txt','r')
filename=[iphone,samsung,lumia,ios,android,windowsphone]

productname=['Iphone','Galaxy','Lumia','Ios','Android','Windowsphone']

outputfile=open('frame1.txt','w')

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
    dictionary['4.Positive percentage']='%.2f%%' % ((float (dictionary['2.Positive']*100))/(float (dictionary['2.Positive']+dictionary['3.Negative'])))
    return dictionary

ph_frame=[]
sys_frame=[]
for i in range(0,3):
    dictionary=creat_dict(filename[i],productname[i],ph_positive,ph_negative)
    ph_frame.append(dictionary)
for i in range(3,6):
    dictionary=creat_dict(filename[i],productname[i],sys_positive,sys_negative)
    sys_frame.append(dictionary)
ph_df=pandas.DataFrame(ph_frame)
sys_df=pandas.DataFrame(sys_frame)

stroutput='%s\n\n\n' % ph_df
outputfile.write(stroutput)
stroutput='%s' % sys_df
outputfile.write(stroutput)
print ph_df
print '\n\n\n'
print sys_df
ph_fpositive.close()
ph_fnegative.close()
sys_fpositive.close()
sys_fnegative.close()
outputfile.close()
for f in filename:
    f.close()    

