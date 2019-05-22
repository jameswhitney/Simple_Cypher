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

