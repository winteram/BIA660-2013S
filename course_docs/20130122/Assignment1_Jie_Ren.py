"""Jie Ren"""
password = str(raw_input('Enter your password(you can inter any character):\n'))
key = str(raw_input('Enter your key(you can inter any charater):\n'))

def encoding(password, key):
    a = password + key
    b = ""
    for i in a[::-1]:
        b += chr(ord(i)+6)
    return b       

print 'After encryption, the password becomes:\n',encoding(password, key)

encoded = raw_input('In the following space, please enter the message you saw above:\n')


def decoding(encoded, key):    
    c = ""
    c_list = list(encoded)
    for i in c_list:
        c += chr(ord(i)-6)
    return c[::-1][0:len(password)]
        
  

print 'After encryption, the password is:\n',decoding(encoded, key)



