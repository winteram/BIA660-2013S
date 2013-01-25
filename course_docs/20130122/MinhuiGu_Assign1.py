"""Simple functions to encode and decode an input string with an input password.
"""

import random

random_map = {}
q = random.randint(1,32)
    
def maplist():
    """Create a dictionary whose values and keys are all range from 32 to 127.
     
    Values have shift right for some positions, which is generated randomly from 1 to 32 
    Return the generated map."""
    global q
    p = {}
    for i in range(32+q,128):
        p[i] = i-q-1
    for i in range (32,32+q+1):
        p[i] = i+127-32-q
    return p
     
def reverse_maplist(dic): 
    """Used to reverse a dictionary, of whose every value is unique.
    
    Return the reversed dictionary after having checked the values to be unique.
    """ 
    li = []
    n = 0
    for k in dic.values():
        li.append(k)
        n = n+1
    for i in range(0,n):
        k = li[i]
        if li.count(k) != 1:
            print "The value of the dic is not unique! can not reverse"
            return
    p = { v:k for k, v in dic.items()}
    return p

def fill_pwd_len(password,length):
    """Modify the password to make the length of the password as specified.
    
    Return the modified password.
    """
    pw = ""
    
    #If password is shorter than that is specified, cycle the password until it is as long as it.
    if len(password) < length:
        for i in range(0,length):
            pw = pw+password[i%(len(password))] 
            
    #If the length of password is longer than that is specified, cut it as required.
    else:
        pw = password[:length]
    return pw
 
def encode(str1, pwd):
    """Encode the input string with the input password.
    
    All the characters whose ascii code range from 32 to 127 is valid for composing
    the string and password. 
    """
    global random_map     
    result = ""   

    #generate the maplist
    random_map = maplist()   
    #modify the password to make it to have the same length as the string
    pwd2 = fill_pwd_len(pwd, len(str1)) 
    #find the values in the maplist using the ascii code of every character as the key for both the string and password
    #for every character in the string, the related values of the character and that of the characters at the same position in password
    #will be added to the encoded string. 
    for i in range (0, len(str1)):
        result = result + chr(random_map[ord(str1[i])]) + chr(random_map[ord(pwd2[i])])
        i = i + 1
    return result        

        
def decode(str1,pwd):
    """Decode the encoded string with the input password.
    
    Encoded string can be decoded to the original string only if the same password is used.
    All the characters whose ascii code range from 32 to 127 is valid for composing
    the string and password. 
    """
    str2 = ""
    global random_map 
    #reverse the maplist
    p2 = reverse_maplist(random_map) 
    #extract the useful part and get the original character using the reversed maplist     
    for i in range (0,len(str1)):
        if i%2 == 0:
            str2 = str2 + chr(p2[ord(str1[i])])
        i = i+1
    return str2        

if __name__ == "__main__":
    teststring = "a~s!sd fa^0sd"
    testpwd = "^ sadf*!(("
    encoded = encode(teststring,testpwd)
    decoded = decode(encoded,testpwd)
    assert(teststring != encode(teststring,testpwd))
    assert(testpwd != encode(teststring,testpwd))
    assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
    assert(teststring == decode(encoded,testpwd))
    #print encoded
    #print decoded
    print "Success!"
