'''
assignment 1
'''
def encode(str):
    strlist=[]
  
    for s in str:
        if s.isalpha():
            input_str=ord(s)
            if (65<=input_str<78) or (97<=input_str<110):
                strlist.append(chr(input_str+15))
            elif (78<=input_str<=90) or (110<=input_str<=122):
                strlist.append(chr(input_str-15))
        else:
            strlist.append(s)
        
    return ''.join(strlist)

    
def decode(str,pwd):
    if(pwd=='password'):
        strlist=[]
        p=[]
        for i in range(len(pwd)):
            p.append(i)
    else:
        return 'wrong!'

#if __name__ == '__main__':
string=raw_input("Please enter a string:")
encodestr=encode(string)
print 'The encoded string is: %strlist' %encodestr
#string='AwodQmdww8'
#encodestr=encode(string)
#print encodestr
password=raw_input("Please enter a password:")
decodestr=decode(encodestr,password)
print decodestr
