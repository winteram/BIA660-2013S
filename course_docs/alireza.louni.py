#Alireza Louni

def    encode(user, password):
       encoded = []
       for i in range(len(user)):
           index_password= password[i % len(password)]
           mixed = chr((ord(user[i]) + ord(index_password)) % 256)#each element of string for both of the user and the password are added together.
        #should be less than 256, so we need to find remainder of 256.
           encoded.append(mixed)#and then put together.
        encoded="".join(encoded)#the output of the last stage is a list, so we need to put together each element of the list to get an encoded string(or list to string conversion)
        return encoded

def     decode(encoded, password):
        decoded= [] #decoded = user
        for i in range(len(encoded)):
          index_password= password[i % len(password)]
          mixed = chr((ord(encoded[i]) - ord(index_password)) % 256)#each element of string for both of the encoded and the password are added together.
        #should be less than 256, so we need to find remainder of 256.
          decoded.append(mixed)#and then put together.
        decoded="".join(decoded)#list to string
        return decoded
