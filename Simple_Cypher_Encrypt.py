################################
# Encrypt a plain text message #
# using a simple Ceaser Cypher #
################################

# import string in order to access builtin string methods
import string


def encrypt(message, shift_value):

    '''
    INPUT: message as string and an int for shift_value
    OUTPUT: Encrypted text based on shift_value for Ceaser Cypher
    '''

    # Convert message string to a list and save to encrypted_message variable
    encrypted_message = list(range(len(message)))

    # Create a lower case alphabet
    alphabet = string.ascii_lowercase

    # Create a shifted version of the alphabet based on the shift_value
    # The shift_value determines where to split the alphabet based on index value
    first_half = alphabet[:shift_value]
    second_half = alphabet[shift_value:]

    shifted_alphabet = second_half + first_half

    # Iterate throught the original message one character at a time.
    # Then assign original alphabet indices to shifted alphabet in order
    # to create an encrypted message based on a Ceaser Cypher

    for i, char in enumerate(message.lower()):

        # Check to see if a character is part of the alphabet.
        # If a character is not part of the alphabet simply
        # add it to the encrypted phrase.

        if char in alphabet:

            # Assign each index for the original alphabet to a variable
            # and then map the original indices to the shifted alphabet
            # to complete the encryption phase

            original_index = alphabet.index(char)
            encrypted_message[i] = shifted_alphabet[original_index]
        
        else:
            # If char is not in alphabet simply assign the character to the encrypted message
            encrypted_message[i] = char

    return ''.join(encrypted_message)


############################################
# This file decrypts the encrypted message #
# from the Simple_Cypher_Encrypt file      #
############################################


def decrypt(message, shift_value):
    '''
    INPUT: Encrypted message from Ceaser Cypher and the integer shift value
    OUTPUT: The decrypted original message
    '''

    # Cast message string to a list and save to a variable
    # for later use
    decrypted_message = list(range(len(message)))

    # Create a list of each individual letter alphabet in original order
    alphabet = string.ascii_lowercase

    # Slice the alphabet based on the shift_value. The first half
    # should be sliced up to the shift_value. The second half
    # should be sliced starting at the shift_value till the end of the string.
    first_half = alphabet[:shift_value]
    second_half = alphabet[shift_value:]

    # Create shifted alphabet by concatenating the second_half of the alphabet
    # with the first_half of the alphabet
    shifted_alphabet = second_half + first_half

    # Iterate over the message string to get the index and characters
    # within the message string
    for i, char in enumerate(message.lower()):

        # If the character is part of the alphabet
        # add it to the decrypted phrase array.
        # If character is not part of the alphabet, add it
        # to the decrypted message.
        if char in alphabet:

            shifted_index = shifted_alphabet.index(char)
            decrypted_message[i] = alphabet[shifted_index]

        else:

            decrypted_message[i] = char

    return ''.join(decrypted_message)


##################################
# Use a brute force method to    #
# decrypt an encrypted message   #
# if encryption key is not known #
##################################


def brute_force_decryption(message):
    '''
    INPUT: A Caeser Cypher encrypted message
    OUTPUT: Prints all possible Ceasar Cypher messages
            Only one output should be the decrypted phrase
    '''
    
    alphabet = list(range(len(string.ascii_lowercase)))
    
    for n in alphabet:
        print('Using shift value: {}'.format(n))
        print(decrypt(message, n))
        print('\n')