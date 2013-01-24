import string
import random

#This function is used for encryption
def encode(password,ekey):
    l=''
    t=''
    p=''
    ek=''
    n=len(str(password))
    l=n
    for ch in ekey:
        ek = int(ord(ch))
    for ch in password :
       t = int(ord(ch))^int(ek)^int(l)
       if t in range (0,127):
           m = chr(t)
           p = p + m
       else:
           print 'Input error!'
    print 'Message', p
    return p

#This function is used for decryption
def decode(cyphertext,dkey):
    l=''
    dk=''
    k=0
    for i in range (3):
        t=''
        p=''
        cyphertext = raw_input('Enter the Message you saw above :')
        dkey = raw_input('Enter the key for password : ')
        l = len(str(cyphertext))
        for ch in dkey:
            dk = int(ord(ch))
        for ch in cyphertext:
            t = int(ord(ch))^int(dk)^int(l)
            m = chr(t)
            p = p + m
        if p==password:
            print 'Successfully decrypt!'
            print 'The password is', p, ', and the key is', dkey, '.'
            return p
        else:
            if k > 3:
                print 'System is going to shut down!'
                quit()
            else:
                k+=1
                print 3-k,'times left! Try again!'
                
        
if __name__=='__main__':
    cyphertext=''
    dkey=''
    password = raw_input('Enter your password: ')
    ekey = raw_input('Enter your key: ')
    encry=encode(password,ekey)
    decry=decode(cyphertext,dkey)
