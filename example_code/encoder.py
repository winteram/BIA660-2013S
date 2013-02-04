def encode(input, password):
    encoded_input = ''
    for i in range(max(len(input),len(password))):
        idxa = i % len(input)
        idxb = i % len(password)
        encoded_input += chr((ord(input[idxa]) + ord(password[idxb])) % 256)

    return encoded_input

def decode(encoded_input, password):
    decoded_input = ''
    for i in range(max(len(encoded_input),len(password))):
        idxa = i % len(encoded_input)
        idxb = i % len(password)
        decoded_input += chr((ord(encoded_input[idxa]) - ord(password[idxb])) % 256)

    return decoded_input

if __name__ == "__main__":
    teststring = "The quick brown 4356 jumped over the lazy dog."
    testpwd = "password"
    encoded = encode(teststring,testpwd)
    assert(teststring != encode(teststring,testpwd))
    assert(testpwd != encode(teststring,testpwd))
    # assert(encode(testpwd,teststring) != encode(teststring,testpwd))
    assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
    assert(teststring == decode(encoded,testpwd))
    print "Success!"
