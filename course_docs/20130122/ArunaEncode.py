

num = 0
mod = 0
textJoin = ''
import random
num = random.randrange(1,10)

def var():
   global num
   global textJoin
   global mod

def encode(text,pwd):
   """ Takes a text and a password.
       Converts the password into it's ASCII value, joins them. A random number is generated which is then mod with the joined number and the result is stored in a variable num. The       string is converted into ASCII and those bits are first reversed abd then shifted as many times as num. 
       Returns an encoded string."""
   global num
   global textJoin
   global mod

   import string
   valJoin = ''.join(str(ord(c)) for c in pwd)
   valNum = string.atoi(valJoin)
   
   mod = valNum % num
  
   textJoin = [ord(c) for c in text]
   textJoin.reverse()

   for i in range(mod):
      popVal = textJoin.pop()
      textJoin.insert(0,popVal) 
   textJoin = ''.join(chr(i) for i in textJoin)
   return textJoin

def decode(enText,pwd):
   """ Takes encoded text and a password.Converts the text into ASCII and the is shifted as many times as num which is a global variable and then the text bits are reversed.
       Returns the decoded string. """
   global num
   global textJoin
   global mod

   import string
   enJoin = [ord(c) for c in enText]

   for i in range(mod):
      enPop = enJoin.pop(0)
      enJoin.append(enPop)
   enJoin.reverse()
   enJoin = ''.join(chr(i) for i in enJoin)   
   return enJoin

if __name__ == "__main__":

   print "Encoded value of the text is %s" % encode('aruna','roomoo')
   print "Decoded value of the text is %s" % decode(textJoin,'roomoo')  
