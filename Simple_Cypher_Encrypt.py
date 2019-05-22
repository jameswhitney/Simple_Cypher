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
