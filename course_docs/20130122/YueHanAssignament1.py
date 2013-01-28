"""
Assignment 1 by Yue Han
Create January 27, 2013
My algorithm is very simple. It is a mirror reverse of the unicode.

"""

def encode(input, password):
	""" Takes two strings and transforms them into a third, encoded string """
	encodeword = input + password
	encodelist = list (encodeword)
	for i in range(0, len(encodelist)):
		encodelist[i] = 32+127-ord(encodelist[i])
	for i in range (0,len(encodelist)):
		encodelist[i] = chr(encodelist[i])
	encoded_string = ''.join(encodelist)

	return encoded_string


def decode(encoded, password):
	""" Takes an encoded string (from encode function) and a password and returns the orginal string"""
	decodelist = list(encoded)
	for i in range(0,len(decodelist)):
		decodelist[i] = 32+127-ord(decodelist[i])
	for i in range (0,len(decodelist)):
		decodelist [i] = chr (decodelist[i])
	decodeword = ''.join(decodelist)
	decoded_string = decodeword[0:(len(decodeword)-len(password))]

	return decoded_string


if __name__ == "__main__":

	teststring = "This is some text to be encoded"
	testpwd = "Password"
	encoded= encode(teststring,testpwd)
	assert(teststring != encode(teststring,testpwd))
	assert(testpwd != encode(teststring,testpwd))
	assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
	assert(teststring == decode(encoded,testpwd))
	print "Success!"