def encode(Input,Password):
    '''
    Encode input by using password
    '''
    s = []   #Intialize a list to store ascii of input
    p = []   #Intialize a list to store ascii of password
    for i in range(len(Input)):
        ''''''
        s.append(ord(Input[i]))

    for i in range(len(Password)):
        p.append(ord(Password[i]))

    for i in range(len(s)):
        for j in range(len(p)):
            # Add p[j] to s[i] if j is a even number
            if(j % 2 == 0):  
                s[i] += p[j]
            else:
                s[i] -= p[j]

    for i in range(len(s)):
        s[i] = str(s[i])+'n'  #Add 'n' to the end of each element of list s

    str1=''.join(s)  #covert list s to string str1
        
    return str1

   
def decode(Encoded_input,Password):
    '''
    Decode the encoded_input by using password
    '''
    if(Password == 'Tjmatrix31'):
        s = Encoded_input.split('n') #split encoded_input to list s
        p = []   #Intialize a list to store ascii of password
        Input = []   #Initialize a list to store decoded input
        for i in range(len(Password)):
            p.append(ord(Password[i]))

        s.pop()
        s = map(int,s)  # convert a list of string to a list of integer
    
        for i in range(len(s)):
            for j in range(len(p)):
                # Substract p[j] to s[i] if j is a even number
                if(j % 2 == 0):
                    s[i] -= p[j]
                else:
                    s[i] += p[j]
            Input.append(chr(s[i])) #Add a character according to its ascii
    
        return ('').join(Input) #convert Input to a string
    else:
        # return mutiple '!' if the password is wrong
        return '!!!!!!!!!!!!, need a correct password'

if __name__ == '__main__':
    '''
    main function
    '''
    originalString = raw_input("Please input the original string: ")
    str2 = encode(originalString,"Tjmatrix31")
    print 'The encoded string is: %s'%str2
    password = raw_input("Please input the password for decoding: ")
    str1 = decode(str2,password)
    print 'The original string is: %s'%str1
