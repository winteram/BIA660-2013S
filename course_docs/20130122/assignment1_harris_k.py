"""
harris kyriakou

Assignment 1
Due January 29, 2013
Create python code that encodes and decodes a string given a password
If you add your code to the 'encode' and 'decode' functions, and run it, it should print 'Success!'

"""

def encode(input, password):
    """ Takes two strings and transforms them into a third, encoded string """
    
    # convert a string to a list of characters
    # set password
    pwd = "saxlamaras11"
    pwd_list = list(pwd)
    
    
    # create a second string to be combined with password (key)    
    key= "ayta1einai1ellinika1kai1mono1ego1ta1katalabaino1"
    key_list =list (key)
    

    # convert characters to integers by using the map function!
    pwd2int = map(ord, pwd_list)
    key2int = map(ord, key_list)    
    
    # combine the key and password strings
    # encoded_string = key2int + pwd2int
    encoded_string = pwd2int[0:1] + key2int + pwd2int[1:]
    return encoded_string




def decode(encoded, password):
    """ Takes an encoded string (from encode function) and a password and returns the original string"""


    # DECODING PART
    pwd2chr = map(chr, encoded_string)
    # chr(ord('a') + 3)


    # find length of encoded string
    len(pwd2chr)

    # convert a list of characters to a string
    s1 = ''.join(pwd2chr[0:1])
    s2 = ''.join(pwd2chr[len(key_list)+1:len(pwd2chr)])


    decoded_string = s1 + s2

    return decoded_string




if __name__ = "__main__":

   teststring = "ayta1einai1ellinika1kai1mono1ego1ta1katalabaino1"
   testpwd = "saxlamaras11"
   assert(teststring != encode(teststring,testpwd))
   assert(testpwd != encode(teststring,testpwd))
   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   assert(teststring == decode(encoded,testpwd))
   print "Success!"