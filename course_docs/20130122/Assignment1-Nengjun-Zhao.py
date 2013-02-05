def encode(s,key):
    b=bytearray(str(s).encode("gbk"))
    n=len(b)
    c=bytearray(n*2)
    j=0
    m=len(c)
    for i in range(0,n):
        b1=b[i]
        b2=b1^key
        c1=b2%16
        c2=b2//16
        c1=c1+65
        c2=c2+65
        i=i+1
        for j in range(0,m):
            c[j]=c1
            c[j+1]=c2
            j=j+2
    return c.decode("gbk")

def jiemi(s, key):
    c = bytearray( str(s).encode("gbk") )
    n = len(c)
    if n % 2 != 0 :
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for j in range(0,n):
        c1 = c[j] 
        c2 = c[j+1] 
        j = j+2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2*16 + c1
        b1 = b2^ key
        for i in range(0,n)
            b[i]= b1
        try: 
            return b.decode("gbk")
        except:
            return "error"


key = 15
s = "holle word"
s1 = jiami( s, key )
s2 = jiemi( s1,key )
print( "input=", s)
print( "password=", s1)
print( "encode:")
print( s2 )