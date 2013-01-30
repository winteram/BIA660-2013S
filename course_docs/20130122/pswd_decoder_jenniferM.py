def encode(input1, password):

    """ Takes two strings and transforms them into a third, encoded string """

    encoded_string = []

    # The first number signifies the length of the password as opposed to making a list of lists 
    encoded_string.append(len(password))

    # Iterate through the letters, encoding them 1 by 1, password first and then the secure message
    for c in (password + input1):

        # Convert the letter to ascii
        encoded_letter = ord(c)

        # Add the ascii value to the above list
        encoded_string.append(encoded_letter)    


    return encoded_string


def decode(encoded, password):

    """ Takes an encoded string (from encode function) and a password and returns the orginal string"""

    # Create a list for the user entered password
    encoded_user_password = []

    # Convert the user entered password to ascii to compare to the encoded password
    # This is done instead of converting the master password to plain text and storing it
    for c in password:

        # Convert the letter to ascii
        encoded_letter = ord(c)

        # Add the ascii value to the above list
        encoded_user_password.append(encoded_letter) 

    # Check if the user's password matches the encoded password
    if encoded_user_password == encoded[1:(encoded[0]+1)]:

        # Create a string that will form the string
        decoded_string = ''

        # Decode the encoded string if passwords match
        for c in encoded[(encoded[0]+1):]:

            # Converts ascii to a letter/character
            decoded_letter = chr(c)

            # Add the letters one by one to form the string 
            decoded_string += decoded_letter
        

    return decoded_string


if __name__ == "__main__":


   teststring = "This is some text to be encoded"

   testpwd = "Password"

    # Added this since this is the encoded message unique to this program
    # This contains the length of the above password, the above password, and the above message
   encoded = [8, 80, 97, 115, 115, 119, 111, 114, 100, 84, 104, 105, 115, 32, 105, 115, 32, 115, 111, 109, 101, 32, 116, 101, 120, 116, 32, 116, 111, 32, 98, 101, 32, 101, 110, 99, 111, 100, 101, 100]

   assert(teststring != encode(teststring,testpwd))

   assert(testpwd != encode(teststring,testpwd))

   assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))

   assert(teststring == decode(encoded,testpwd))

   print "Success!"
