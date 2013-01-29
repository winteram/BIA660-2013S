"""
Assignment 1
Author : Priyanka K
Python code that encodes and decodes an input string given a password

"""

def encode(input, password):
    """ Encode function takes input string and password and transforms them into a third, encoded string """
    """ The logic used to encode a string is to decrease the ASCII of password by 1 and increase the ASCII for each character in the input string by 1 
        and then combine both with a '^' character. Finally display the concatenated string.
    """
    input_str = [ord(c)+1 for c in input]
    encoded_pass = [ord(c)-1 for c in password]
    encoded_pass = [chr(p) for p in encoded_pass]
    encoded_pass="".join(encoded_pass)
    encoded_str = [chr(c) for c in input_str]
    encoded_str ="".join(encoded_str)
    encoded_string = encoded_pass+'^'+encoded_str
    return encoded_string
  
    

def decode(encoded, password):
    """ Decode function takes an encoded string and a password and returns the orginal string """
    """ The logic used to decode the string, is to first split the encoded string on '^' which connects the password and the input string.
        Then get the first element, which is the decoded password, and convert it back to original value by incrementing its ASCII.
        Next compare this password with the original password to check if they match.
        In case of success, decode the input string by subtracting it by one character position.
        In case of no match, print Invalid password.
    """
    input_str = encoded.split('^')
    decoded_pass = input_str[0]
    decoded_pass = [ord(c) for c in decoded_pass]
    decoded_pass = [chr(c+1) for c in decoded_pass]
    decoded_pass = "".join(decoded_pass)
    if(decoded_pass == password):
        decoded_input = [ord(c) for c in input_str[1]]
	decoded_input = [chr(c-1) for c in decoded_input]
	decoded_string = "".join(decoded_input)
    	return decoded_string
    return "Invalid password!!"


if __name__ == "__main__":

   teststring = "This is some text to be encoded"
   testpwd = "Password"
   assert(teststring != encode(teststring,testpwd))
   assert(testpwd != encode(teststring,testpwd))
   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   encoded = encode(teststring,testpwd)
   assert(teststring == decode(encoded,testpwd))
   print "Success!"
