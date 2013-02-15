"""
Assignment 1
Mahdi Azarafrooz
"""
def encode(text, password):
    s=0
    for i in range(len(password)):
        s+=ord(password[i])
        
        
    encoded_text=''
    
    for i in range(len(text)):
        c=ord(text[i])+s
        c=c%128
        encoded_text+=chr(c)
        
    return encoded_text


def decode(encoded_text, password):
    s=0
    for i in range(len(password)):
        s+=ord(password[i])
    
    text=''
    for i in range(len(encoded_text)):
        c=ord(encoded_text[i])-s
        c=c%128
        text+=chr(c)
             

    return text 
