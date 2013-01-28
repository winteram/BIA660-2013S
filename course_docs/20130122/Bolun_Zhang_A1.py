"""
Name: Bolun Zhang
"""
"""
Assignment 1
Due January 29, 2013

Create python code that encodes and decodes a string given a password
If you add your code to the 'encode' and 'decode' functions, and run it, it should print 'Success!'

"""
"""
Transfer the input and password into ASCII, and use the ASCII code to do the encoding and decoding
"""
def encode(input, password):
    """ Takes two strings and transforms them into a third, encoded string """
    inp = input
    psw = password
    encoded_string = ''
    inp_list = list(range(0))
    psw_list = list(range(0))
    for i in range(0,len(inp),1):
        #print a[i]
        #print ord(a[i])
        inp_list.append(ord(inp[i]))
        
    for i in range(0,len(psw),1):
        psw_list.append(ord(psw[i]))
    
    #transfer input and password into ASCII code 
        
    for i in range(0,len(inp),1):
        for j in range(0,len(psw),1):
            if psw_list[j]%2==0:
                inp_list[i] = inp_list[i] + psw_list[j]%5
            else:
                inp_list[i] = inp_list[i] - psw_list[j]%4
    #encoding by ASCII code 
                
    for i in range(0,len(inp),1):
        encoded_string = encoded_string + chr(inp_list[i])

    return encoded_string


def decode(encoded, password):
    """ Takes an encoded string (from encode function) and a password and returns the orginal string"""

    decoded_string = ''
    enc = encoded
    psw = password
    enc_list = list(range(0))
    psw_list = list(range(0))
    for i in range(0,len(enc),1):
        enc_list.append(ord(enc[i]))
        
    for i in range(0,len(psw),1):
        psw_list.append(ord(psw[i]))
    
    for i in range(0,len(enc),1):
        for j in range(0,len(psw),1):
            if psw_list[j]%2==0:
                enc_list[i] = enc_list[i] - psw_list[j]%5
            else:
                enc_list[i] = enc_list[i] + psw_list[j]%4
    #decoding by ASCII code
    
    for i in range(0,len(enc),1):
        decoded_string = decoded_string + chr(enc_list[i])

    return decoded_string


if __name__ == "__main__":
    teststring = "This is some text to be encoded"
    testpwd = "Password"
    encoded = encode(teststring,testpwd)
    decoded = decode(encoded, testpwd)
    print "the encoded text is: "+encoded
    print "the decoded text is: "+decoded
    assert(teststring != encode(teststring,testpwd))
    assert(testpwd != encode(teststring,testpwd))
    assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
    assert(teststring == decode(encoded,testpwd))
    print "Success!"



"""
output:
the encoded text is: K_`j`jjfd\k\okkfY\\eZf[\[
the decoded text is: This is some text to be encoded
Success!
"""