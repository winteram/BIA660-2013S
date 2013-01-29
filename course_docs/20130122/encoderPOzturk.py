"""
Pinar Ozturk - Simple XOR encryption

Assignment 1
Due January 29, 2013

Create python code that encodes and decodes a string given a password
If you add your code to the 'encode' and 'decode' functions, and run it, it should print 'Success!'

"""

def encode(input, password):
    """ Takes two strings and transforms them into a third, encoded string """

    encoded_string = ''

    for char in input:
        for char1 in password:
            char=chr(ord(char)^ord(char1))
        encoded_string +=char

    return encoded_string


def decode(encoded_string, password):
    """ Takes an encoded string (from encode function) and a password and returns the orginal string"""

    decoded_string = ''

    for char in encoded_string:
        for char1 in password:
            char=chr(ord(char)^ord(char1))
        decoded_string +=char

    return decoded_string


if __name__ == "__main__":

   teststring = "This is some text to be encoded"
   testpwd = "Password"
   encoded_string=encode(teststring,testpwd)
   decoded_string=decode(encoded_string,testpwd)
   print "The encoded message is:" + encoded_string
   print "The decoded message is: " + decoded_string
   assert(teststring != encode(teststring,testpwd))
   assert(testpwd != encode(teststring,testpwd))
   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   assert(teststring == decode(encoded_string,testpwd))
   print "Success!"
