# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def encode(inputString, password):
    """ Takes two strings and transforms them into a third, encoded string """
    s2=",".join(str(ord(ch)) for ch in inputString)
    s3=",".join(str(ord(ch)) for ch in password)
    s4=s2+"&"+s3   
    encoded_string = s4
    return encoded_string


def decode(encoded, password):
    """ Takes an encoded string (from encode function) and a password and returns the orginal string"""
    li=encoded.split("&")
    input_list=li[0].split(",")
    pswd_list=li[1].split(",")
    input_string="".join(chr(int(input_list[i])) for i in range(len(input_list)))
    pswd_string="".join(chr(int(pswd_list[i])) for i in range(len(pswd_list)))
    
    if pswd_string == password :
        return input_string
    else:
        return "DECODING FAILED"
        
        


if __name__ == '__main__':
    teststring = "This is some text to be encoded"
    testpwd = "Password"     
    assert(teststring != encode(teststring,testpwd))
    assert(testpwd != encode(teststring,testpwd))
    assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))    
    encodedString = encode(teststring,testpwd)    
    assert(decode(encodedString,"wrongpwd") !=decode(encodedString,testpwd) )
    assert(teststring == decode(encode(teststring,testpwd),testpwd))
    print "Success!"

# <codecell>


