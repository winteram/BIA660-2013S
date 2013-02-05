# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def encode(input, password):
    encoded_input = ''
    for i in range(max(len(input),len(password))):
        idxa = i % len(input)
        idxb = i % len(password)
        encoded_input += chr(32 + (((ord(input[idxa]) + ord(password[idxb])-32)) % 94))

    return encoded_input

# <codecell>

def decode(encoded_input, password):
    decoded_input = ''
    for i in range(max(len(encoded_input),len(password))):
        idxa = i % len(encoded_input)
        idxb = i % len(password)
        decoded_input += chr(32 + (((ord(encoded_input[idxa]) - ord(password[idxb])-32)) % 94))

    return decoded_input

# <codecell>

teststring = "The quick brown 4356 jumped over the lazy dog."
testpwd = "password"

# <codecell>

encode(teststring,testpwd)

# <codecell>

encoded = encode(teststring,testpwd)

# <codecell>

decode(encoded,testpwd)

# <codecell>

encode("The quick","Dog")

# <codecell>

tmp = ''
for i in range(32,126):
    tmp += chr(i)
print tmp

# <codecell>

ord("T")

# <codecell>

ord("D")

# <codecell>

84+68

# <codecell>

(84+68-32) % 94 + 32

# <codecell>

chr(58)

# <codecell>

def alt_encode(input,pwd):
    encoded_string = input[1:7]+input[-0]+" "+pwd[1:8]+pwd[-0]
    return encoded_string

print "this is always printed"

# <codecell>

alt_encode("NewYork","Yankees")

# <codecell>


