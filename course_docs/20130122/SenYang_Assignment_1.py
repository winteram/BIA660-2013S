"""
Created on Jan 22, 2013
@author: senyang
Description: The following is my algorithm: I build two lists (name: source and data). Each list stores 
the Ascii table in the range of 32-126. The difference between these lists is the order of elements
in first list(source) is constant, the elements'order in the second list(data) is random. But the numbers
of these elements in both lists are same. When I encode, I combine the string inputted with password
to generate a new string. And then I compare every letter in the new string with the source and get these
elements' indexes in the source list. Finally I find the corresponding value in the data list according to 
these indexes and generate the encoded string. The decode function is opposite. The extra step of decode
function is to verify if the password is right. Then this function could output the decoded string 
or the error warning. Please review my codes to check these two functions. Thank you!

"""

#Generate Ascii table list in the range of 32-126
ascnum = range(32,127)
source = []
for a in ascnum:
    b = chr(a)
    source.append(b)


#Generate corrospoding random Ascii table list in range 32-126
import random
data = source[:]
random.shuffle(data)



#encode function
def encode(inpt,password):
    encoded_string = ''
    combine =  inpt + password;  
    l1 = list(combine)
    for i in l1:
        for j in source:
            if j == i:
                source_elemt_index = source.index(j, )
                value_in_data = data[source_elemt_index]
                encoded_string += value_in_data
                break 
    return encoded_string 

#decode function
def decode(encoded,password):
    decoded_string = ''
    l2 = list(encoded)   
    for i in l2:
        for j in data:
            if j == i:
                data_elemt_index = data.index(j,)
                value_in_source = source[data_elemt_index]
                decoded_string += value_in_source
                break
    # Verify if password exist in the decoded string        
    is_exist = decoded_string.find(password)
    if is_exist == -1:
        decoded_string = ''
    else:
        decoded_string = decoded_string[0:is_exist]
                
    return decoded_string
        
#----------My Testing Codes----------              
in_str = 'This is some text to be encoded'
pwd = 'password'    
print 'input=====  ' + in_str
encoded = encode(in_str,pwd)
print 'encoded===  ' + encoded
decoded = decode(encoded,pwd)

if decoded == '':
    print 'Wrong Password, Please try again!'
else:
    print 'decoded===  '+decoded

print '\n'
    
#Testing Module
if __name__ == "__main__":
    teststring = "This is some text to be encoded"
    testpwd = "Password"
    encoded = encode(teststring,testpwd)
    assert(teststring != encode(teststring,testpwd))
    assert(testpwd != encode(teststring,testpwd))
    assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
    assert(teststring == decode(encoded,testpwd))
    print "Success!"

