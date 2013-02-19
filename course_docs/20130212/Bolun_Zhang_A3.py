'''
Created on Feb 12, 2013

@author: zbl
'''



#def testEmail():
import re
ph_str = "^[0-9"
ph_str += "\a-z\-\.\+\_]"
    #ph_str ="\zhangkakashhi1]"
ph_str += "{5,14}"
ph_str += "[(@)]{1}"
ph_str += "[a-z\0-9]{2,7}"
ph_str += "[(.)]{1}"
ph_str += "[edu\com\cn\com.cn]{2,6}$"
phone = re.compile(ph_str)
fh = open('testEmail.txt','r')
phones = fh.readlines()
for ph in phones:
    if phone.match(ph):
        print"correct: %s" % ph
    else:
        print"incorrect: %s" % ph
    #return
        
#if __name__=="__main__":
   # testEmail()