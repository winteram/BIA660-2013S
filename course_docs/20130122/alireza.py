#Alireza Louni

def     encode(user, password):
        encoded = []
        for i in range(len(user)):
            index_password= password[i % len(password)] # we need to obtain remainder (%) since "password" and "user" might have different letter long.
            mixed = (ord(user[i]) + ord(index_password)) % 256 #each element of string for both of the user and the password are added together.
            mixed_char=chr(mixed)
       #should be less than 256, so we need to find remainder of 256.
            encoded.append(mixed_char)#and then put together.
        encoded="".join(encoded)#the output of the last stage is a list, so we need to put together each element of the list to get an encoded string(or list to string conversion)
        return encoded

def     decode(encoded, password):
        decoded= [] #decoded = user
        for i in range(len(encoded)):
            index_password= password[i % len(password)]
            mixed = (ord(encoded[i]) - ord(index_password)) % 256 #each element of string for both of the encoded and the password are added together.
        #should be less than 256, so we need to find remainder of 256.
            mixed_char=chr(mixed)
            decoded.append(mixed_char)#and then put together.
        decoded="".join(decoded)#list to string
        return decoded #returns original user name.

if __name__ == '__main__':

   teststring = "This is some text to be encoded"
   testpwd = "Password"
   encoded = encode(teststring,testpwd)
   assert(teststring != encoded)
   assert(testpwd != encode(teststring,testpwd))
   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   assert(teststring == decode(encoded,testpwd))
   print "Success!"
