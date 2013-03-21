import pandas
import numpy as np
import matplotlib.pyplot as plt
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
    
def creat_dict(filename,dproduct,positive,negative):
    global pos_frame
    global neg_frame

    for p in range(0,len(positive)):
        pos_frame[p][dproduct]=0
    for p in range(0,len(negative)):
        neg_frame[p][dproduct]=0
            
    line=filename.readline()
    while line:
        for p in range(0,len(positive)):
            if re.findall(positive[p],line):
                pos_frame[p][dproduct] +=1
        for p in range(0,len(negative)):
            if re.findall(negative[p],line):
                neg_frame[p][dproduct] +=1
        line=filename.readline()
    pos_total=0
    neg_total=0
    for p in range(0,len(positive)):
        pos_total +=pos_frame[p][dproduct]
    for p in range(0,len(negative)):
        neg_total +=neg_frame[p][dproduct]
    
    for p in range(0,len(positive)):
        percent='%.2f' % ((float (pos_frame[p][dproduct]*100))/(float (pos_total)))
        pos_frame[p][dproduct]=float(percent)
    for p in range(0,len(negative)):
        percent='%.2f' % ((float (neg_frame[p][dproduct]*100))/(float (neg_total)))
        neg_frame[p][dproduct]=float(percent)
    
#for phone
pos_frame=[]
neg_frame=[]
for word in ph_positive:
    pos_frame.append({})
for word in ph_negative:
    neg_frame.append({})
for i in range(0,3):
    creat_dict(filename[i],productname[i],ph_positive,ph_negative)
ph_pos_df=pandas.DataFrame(pos_frame)
ph_neg_df=pandas.DataFrame(neg_frame)

#for system
pos_frame=[]
neg_frame=[]
for word in sys_positive:
    pos_frame.append({})
for word in sys_negative:
    neg_frame.append({})
for i in range(3,6):
    creat_dict(filename[i],productname[i],sys_positive,sys_negative)
sys_pos_df=pandas.DataFrame(pos_frame)
sys_neg_df=pandas.DataFrame(neg_frame)

ph_pos_ind=[]
ph_neg_ind=[]
sys_pos_ind=[]
sys_neg_ind=[]
for i in range(0,3):
    ph_pos_ind.append(np.arange(0.3*i,len(ph_positive)+0.3*i))
    ph_neg_ind.append(np.arange(0.3*i,len(ph_negative)+0.3*i))
    sys_pos_ind.append(np.arange(0.3*i,len(sys_positive)+0.3*i))
    sys_neg_ind.append(np.arange(0.3*i,len(sys_negative)+0.3*i))
    
bar_color=['r','g','y']

#for phone
pos_product_bar=[]
neg_product_bar=[]

plt.figure(figsize=(20,15))
for i in range(0,3):
    bar_chart=plt.bar(ph_pos_ind[i],ph_pos_df[productname[i]],0.3,color=bar_color[i])
    pos_product_bar.append(bar_chart[0])
plt.xlabel('Positive Words')
plt.ylabel('Percentage in Total Positive Words(%)')
plt.title('Positive Aspects of Three Brands of Phone')
plt.xticks(ph_pos_ind[0]+0.45,(ph_positive))
plt.legend((pos_product_bar),(productname[0:3]))
plt.savefig('ph_pos_bar.png')

plt.figure(figsize=(20,15))
for i in range(0,3):
    bar_chart=plt.bar(ph_neg_ind[i],ph_neg_df[productname[i]],0.3,color=bar_color[i])
    neg_product_bar.append(bar_chart[0])
plt.xlabel('Negative Words')
plt.ylabel('Percentage in Total Negative Words(%)')
plt.title('Negative Aspects of Three Brands of Phone')
plt.xticks(ph_neg_ind[0]+0.45,(ph_negative))
plt.legend((neg_product_bar),(productname[0:3]))
plt.savefig('ph_neg_bar.png')

#for system
pos_product_bar=[]
neg_product_bar=[]

plt.figure(figsize=(20,15))
for i in range(0,3):
    bar_chart=plt.bar(sys_pos_ind[i],sys_pos_df[productname[i+3]],0.3,color=bar_color[i])
    pos_product_bar.append(bar_chart[0])
plt.xlabel('Positive Words')
plt.ylabel('Percentage in Total Positive Words(%)')
plt.title('Positive Aspects of Three Phone Systems')
plt.xticks(sys_pos_ind[0]+0.45,(sys_positive))
plt.legend((pos_product_bar),(productname[3:6]))
plt.savefig('sys_pos_bar.png')

plt.figure(figsize=(20,15))
for i in range(0,3):
    bar_chart=plt.bar(sys_neg_ind[i],sys_neg_df[productname[i+3]],0.3,color=bar_color[i])
    neg_product_bar.append(bar_chart[0])
plt.xlabel('Negative Words')
plt.ylabel('Percentage in Total Negative Words(%)')
plt.title('Negative Aspects of Three Phone Systems')
plt.xticks(sys_neg_ind[0]+0.45,(sys_negative))
plt.legend((neg_product_bar),(productname[3:6]))
plt.savefig('sys_neg_bar.png')
ph_fpositive.close()
ph_fnegative.close()
sys_fpositive.close()
sys_fnegative.close()
for f in filename:
    f.close() 
