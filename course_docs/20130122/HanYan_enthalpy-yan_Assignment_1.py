'''
My encryption is a very simple Caesar Cipher 
'''

#generate all of the prospective character from asc ii code 
key = [chr(i) for i in range(32,127)]
#used to save the new key list
new_key = []
#used to check whether the password is right or wrong
check_key = []
#used to save encrypted input
encrypt_input = " "
#used to save decrypted input
decrypt_output = " "

#This function is used to change key's order saved in new_key
def change_order(list, num):
    global new_key
    list1 = []
    list1 += list
    for i in range(num):
        list1.append(list1[0])
        list1.remove(list1[0])
    new_key = list1;
    
#This function is used to change new_key's order saved in check_key
def change_order_r(list, num):
    global check_key
    list1 = []
    list1 += list
    for i in range(num):
        c = list1.pop()
        list1.insert(0, c)
    check_key = list1;

def encode(input, password):
    global key   
    global encrypt_input  
    global new_key
    encrypt_list = []
    list_input = list(input)
    str_pd = list(password)
    num_pd = 0
    
    #calculate the shift number of Caesar Cipher
    for character in str_pd:
        num_pd += ord(character)
        num_pd = num_pd % 19
        if num_pd == 0:
            num_pd = 20
    change_order(key, num_pd)
    
    #from new_key to generate new string 
    for c in list_input:
        if c not in key:
            encrypt_list.append(c)
        encrypt_list.append(new_key[key.index(c)]);
    encrypt_input = "".join(encrypt_list)
    
    return encrypt_input

def decode(input, password):
    global key
    global new_key
    global decrypt_output
    str_pd = list(password)
    num_pd = 0
    
    #calculate the shift number of Caesar Cipher
    for character in str_pd:
        num_pd += ord(character)
        num_pd = num_pd % 19
        if num_pd == 0:
            num_pd = 20
            
    #from new_key generate the ckeck_key
    change_order_r(new_key, num_pd)
    
    #check whether check_key equals to key
    if check_key != key:
        print "Your password is wrong!"
        return
    decrypt_list = []
    list_input = list(input);
    
    #from new_key's index to calculate the plaintext
    for c in list_input:
        decrypt_list.append(key[new_key.index(c)])
    decrypt_output = "".join(decrypt_list)
    
    return decrypt_output

if __name__ == '__main__':

   teststring = "This is some text to be encoded"
   testpwd = "Password"
   encoded = encode(teststring,testpwd)
   assert(teststring != encoded)
   assert(testpwd != encode(teststring,testpwd))
   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   assert(teststring == decode(encoded,testpwd))
   print "Success!"
   