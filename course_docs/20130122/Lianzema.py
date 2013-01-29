"""
Assignment 1
Due January 29, 2013

Create python code that encodes and decodes a string given a password
If you add your code to the 'encode' and 'decode' functions, and run it, it should print 'Success!'

"""

def encode(input, password):
    """ Takes two strings and transforms them into a third, encoded string """
    password_split=list(password)
    sum_num=0
    encoded_string=''
    for i in password_split:
        sum_num=sum_num+ord(i)
    x=sum_num%26
    input_split=list(input)
    for i in input_split:
        if ord(i)>64 and ord(i)<91:
            if ord(i)+x>90:
                encoded_string+=chr(64+ord(i)+x-90)
            else:
                encoded_string+=chr(ord(i)+x)
        elif ord(i)>96 and ord(i)<123:
            if ord(i)+x>122:
                encoded_string+=chr(96+ord(i)+x-122)
            else:
                encoded_string+=chr(ord(i)+x)
        else:
            encoded_string+=i
            
    return encoded_string


def decode(encoded, password):
    """ Takes an encoded string (from encode function) and a password and returns the orginal string"""
    password_split=list(password)
    sum_num=0
    decoded_string=''
    for i in password_split:
        sum_num=sum_num+ord(i)
    x=sum_num%26
    encoded_split=list(encoded)
    for i in encoded_split:
        if ord(i)>64 and ord(i)<91:
            if ord(i)-x<65:
                decoded_string+=chr(91-(65-(ord(i)-x)))
            else:
                decoded_string+=chr(ord(i)-x)
        elif ord(i)>96 and ord(i)<123:
            if ord(i)-x<97:
                decoded_string+=chr(123-(97-(ord(i)-x)))
            else:
                decoded_string+=chr(ord(i)-x)
        else:
            decoded_string+=i
    
    return decoded_string


if __name__ == "__main__":

   teststring = "This is some text to be encoded"
   testpwd = "Password"
   assert(teststring != encode(teststring,testpwd))
   assert(testpwd != encode(teststring,testpwd))
   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   encoded=encode(teststring,testpwd)
   print encoded
   print decode(encoded,testpwd)
   assert(teststring == decode(encoded,testpwd))
   print "Success!"
