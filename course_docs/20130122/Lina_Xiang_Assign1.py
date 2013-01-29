def encode():
    """encode the string with password provided"""
    oristr = raw_input ('The original string is: ')
    password = raw_input ('The encryption key: ')
    l1=len(oristr)
    l2=len(password)
    if (l1>l2): password = password * (int(l1/l2)+1)
    base=("A","a")
    encodestr = ""
    for i in range(l1):
        if(oristr[i]!=" "):
            number1=ord(oristr[i])
            number2=ord(password[i])
            ps=number1 - number2
            if(number1<number2):
                key=0
            else:
                key=1
            newstr=base[key]+chr(48+abs(ps))
            encodestr = encodestr+newstr
        else:
            encodestr = encodestr+"FF"
    print "encoded string is %s "  % (encodestr)
    return encodestr

def decode(encodedstr, password):
    """decode a encrypted string with its password"""
    l1=len(encodedstr)
    l2=len(password)
    if (l1/2>l2): password = password * (int(l1/2/l2)+1)
    base=("A","a")
    decodestr = ""
    for i in range(l1/2):
        if (encodedstr[2*i] != "F"):
            number1=ord(encodedstr[2*i+1])
            number2=ord(password[i])
            ps=number1 - number2
            if("A"==encodedstr[2*i]):
                key=48+number2-number1
            else:
                key=number1+number2-48
            newstr=chr(key)
        else:
            newstr=" "
        decodestr = decodestr+newstr
    print "decoded string is %s" % (decodestr)
    return decodestr
