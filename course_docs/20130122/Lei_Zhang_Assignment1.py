"""
My algorithm is to randomly generate a dictionary as code dictionary according
to the ASCii table. The encoded string is a combination of username and
password.
"""
import random



#The function used to build encode dictionary in a random way.
def randomList(a1,a2):
    list=[chr(i) for i in range(a1,a2)]
    dic={}
    for i in range(a1,a2):
        dic[i]=random.choice(list)
        list.remove(dic[i])
    return dic

#The function used to build decode dictionary
def reverse_randomList(dic):
    reverse_dic={}
    for key,value in dic.items():
        reverse_dic[value]=key
    return reverse_dic

def encode(username,password):
    Usr=list(username)
    Pwd=list(password)
    for i in range(0,len(Usr)):
        Usr[i]=ord(Usr[i])
    for j in range(0,len(Pwd)):
        Pwd[j]=ord(Pwd[j])
    for i in range(0,len(Usr)):
        Usr[i]=keyList[Usr[i]]
    for j in range(0,len(Pwd)):
        Pwd[j]=keyList[Pwd[j]]
    Usr=''.join(Usr)
    Pwd=''.join(Pwd)

    #The encode string is combination of username and password
    encode_string=Usr+Pwd
    
    return encode_string

def decode(encoded, password):
    decoded=list(encoded)
    password=list(password)
    length=len(password)
    decoded=decoded[:-length]
    for i in range(0,len(decoded)):
        decoded[i]=r_keyList[decoded[i]]
    for i in range(0,len(decoded)):
        decoded[i]=chr(decoded[i])
    decoded_string=''.join(decoded)
    return decoded_string

#   randomly create encode dictionary at the beginning
keyList=randomList(32,128)
#   create decode dictionary according to the keyList 
r_keyList=reverse_randomList(keyList)

if __name__ == "__main__":

    teststring = "This is some text to be encoded"
    testpwd = "Password"
    encoded= encode(teststring,testpwd)
    assert(teststring != encode(teststring,testpwd))
    assert(testpwd != encode(teststring,testpwd))
    assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
    assert(teststring == decode(encoded,testpwd))
    print "Success!"



