#Ebrahim Safavi 
# 1st assignment

def encode(s, p):
    e_s=''
    j=0
    for i in s:
        c=ord(i)+ord(p[j%len(p)])
        c=c%128
        e_s+=chr(c)
        j+=1
        

    return e_s 

def decode(e_s, p):
    s=''
    j=0
    for i in e_s:
        c=ord(i)-ord(p[j%len(p)])
        c=c%128
        s+=chr(c)
        j+=1
        

    return s 
