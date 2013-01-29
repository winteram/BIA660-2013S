"""
Name:Yulong Luo
10374845

"""

"""this function is to reverse the ascii of the char of string"""
def re_ascii(string):
    reverse_str=''
    for char in string:
        reverse_str +=chr(126+32-ord(char))

    return reverse_str

        

def encode(input, password):
    re_input=re_ascii(input)
    re_password=re_ascii(password)
    
    encoded_string = re_input + re_password

    return encoded_string


def decode(encoded, password):
    string=''
    encoded_list=list(encoded)  #transfer string to list
    re_password=re_ascii(password)
    re_password_len=len(re_password)  #get password length
    encoded_list_len=len(encoded_list) #get encoded length
    while re_password_len>0:
        if re_password[re_password_len-1]==encoded_list[encoded_list_len-1]:
            del encoded_list[encoded_list_len-1]
        encoded_list_len -=1
        re_password_len -=1
    for char in encoded_list:
        string +=char
            
    decoded_string = re_ascii(string)

    return decoded_string


if __name__ == "__main__":

   teststring = "dsfsf#@$3"
   testpwd = "EWDSDS1232"
   encoded= encode(teststring,testpwd)
   assert(teststring != encode(teststring,testpwd))
   assert(testpwd != encode(teststring,testpwd))
   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   assert(teststring == decode(encoded,testpwd))
   print "Success!"

