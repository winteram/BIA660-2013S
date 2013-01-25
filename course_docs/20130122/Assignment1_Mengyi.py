"""
Assignment 1
Mengyi Gong

Create python code that encodes and decodes a string given a password
If you add your code to the 'encode' and 'decode' functions, and run it, it should print 'Success!'

"""

# My encoding method is to insert the password into one random spot in the original string. After the insertion, 
# the encode function passes the spot of the insertion to the decode function. By removing the password accordingly, 
# we can get the original string back.

# When running the .py program, reinstating the "print" sentences marked as annotations will show the results of random
# insertions.

import random

insert_spot=0

def encode(input, password):
    """ Takes two strings and transforms them into a third, encoded string """
    
    global insert_spot
    insert_spot=random.randrange(0,len(input))
    
    before_insert_spot=input[0:insert_spot]
    after_insert_spot=input[insert_spot:len(input)]
    
    encoded_string = before_insert_spot+password+after_insert_spot
    #print encoded_string
    #print insert_spot
    
    return encoded_string


def decode(encoded, password):
    """ Takes an encoded string (from encode function) and a password and returns the orginal string"""
    
    decoded_string = encoded[0:insert_spot]+encoded[(insert_spot+len(password)):len(encoded)]
    #print decoded_string
    #print insert_spot

    return decoded_string


if __name__ == "__main__":

   teststring = "This is some text to be encoded"
   testpwd = "Password"
   
   assert(teststring != encode(teststring,testpwd))
   assert(testpwd != encode(teststring,testpwd))
   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   encoded=encode(teststring,testpwd)
   assert(teststring == decode(encoded,testpwd))
   print "Success!"


