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

outputfile=open('frame2.txt','w')

count=2
    
def creat_dict(filename,product,positive,negative):
    global count
    global pos_frame
    global neg_frame
    
    dproduct='%d.%s' % (count,product)
    count +=1
    for p in range(0,len(positive)):
        pos_frame[p][dproduct]=0
    for p in range(0,len(negative)):
        neg_frame[p][dproduct]=0
            
    line=filename.readline()
    while line:
        for p in range(0,len(positive)):
            ret=re.findall(positive[p],line)
            if ret:
                pos_frame[p][dproduct] +=len(ret)
        for p in range(0,len(negative)):
            ret=re.findall(negative[p],line)
            if ret:
                neg_frame[p][dproduct] +=len(ret)
        line=filename.readline()
    pos_total=0
    neg_total=0
    for p in range(0,len(positive)):
        pos_total +=pos_frame[p][dproduct]
    for p in range(0,len(negative)):
        neg_total +=neg_frame[p][dproduct]
    pos_frame[len(positive)][dproduct]=pos_total
    neg_frame[len(negative)][dproduct]=neg_total
    
    for p in range(0,len(positive)):
        percent='%.2f%%' % ((float (pos_frame[p][dproduct]*100))/(float (pos_total)))
        pos_frame[p][dproduct]='%d(%s)' % (pos_frame[p][dproduct],percent)
    for p in range(0,len(negative)):
        percent='%.2f%%' % ((float (neg_frame[p][dproduct]*100))/(float (neg_total)))
        neg_frame[p][dproduct]='%d(%s)' % (neg_frame[p][dproduct],percent)
    
#for phone
pos_frame=[]
neg_frame=[]
for word in ph_positive:
    pos_frame.append({'1.Positive':word})
for word in ph_negative:
    neg_frame.append({'1.Negative':word})
pos_frame.append({'1.Positive':'Total'})
neg_frame.append({'1.Negative':'Total'})
for i in range(0,3):
    creat_dict(filename[i],productname[i],ph_positive,ph_negative)
ph_pos_df=pandas.DataFrame(pos_frame)
ph_neg_df=pandas.DataFrame(neg_frame)

#for system
pos_frame=[]
neg_frame=[]
for word in sys_positive:
    pos_frame.append({'1.Positive':word})
for word in sys_negative:
    neg_frame.append({'1.Negative':word})
pos_frame.append({'1.Positive':'Total'})
neg_frame.append({'1.Negative':'Total'})
for i in range(3,6):
    creat_dict(filename[i],productname[i],sys_positive,sys_negative)
sys_pos_df=pandas.DataFrame(pos_frame)
sys_neg_df=pandas.DataFrame(neg_frame)

stroutput='%s' % ph_pos_df
outputfile.write(stroutput)
outputfile.write('\n\n\n')
stroutput='%s' % ph_neg_df
outputfile.write(stroutput)
outputfile.write('\n\n\n')
stroutput='%s' % sys_pos_df
outputfile.write(stroutput)
outputfile.write('\n\n\n')
stroutput='%s' % sys_neg_df
outputfile.write(stroutput)

print ph_pos_df
print '\n\n\n'
print ph_neg_df
print '\n\n\n'
print sys_pos_df
print '\n\n\n'
print sys_neg_df
ph_fpositive.close()
ph_fnegative.close()
sys_fpositive.close()
sys_fnegative.close()
outputfile.close()
for f in filename:
    f.close() 
