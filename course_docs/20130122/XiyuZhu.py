#This function is used for encryption
def encode(teststring,testpwd):
    t=''
    p=''
    ek=0
    offset=0
    for ch in testpwd:
        ek += int(ord(ch))
    offset = ek % len(testpwd)
    for ch in teststring:
        rec = 0
        rec = (int(ord(ch))+offset)%127
        if rec in range (32+offset,126):
           m = chr(rec)
           p = p + m
        else:
           rec = rec+32
           m = chr(rec)
           p = p + m
    return p

#This function is used for decryption
def decode(encoded,testpwd):
    dk=0
    offset=0
    p=''
    for ch in testpwd:
        dk += int(ord(ch))
    offset = dk % len(testpwd)
    for ch in encoded:
        t = 0
        t = (int(ord(ch))-offset)%127
        if t in range (32,126-offset):
            m = chr(t)
            p = p + m
        else:
            t = t-offset+95
            m = chr(t)
            p = p + m
    return p
                    

if __name__ == "__main__":
    teststring = "This is some text to be encoded"
    testpwd = "Password"
    encoded = encode(teststring,testpwd)
    decoded = decode(encoded,testpwd)
    assert(teststring != encode(teststring,testpwd))
    assert(testpwd != encode(teststring,testpwd))
    assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
    assert(teststring == decode(encoded,testpwd))
    print "Success!"
