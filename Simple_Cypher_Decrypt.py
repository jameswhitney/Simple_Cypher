
############################################
# This file decrypts the encrypted message #
# from the Simple_Cypher_Encrypt file      #
############################################

import string

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