
################################
# Use a brute force method to  #
# decrypt an encrypted message #
################################

import string
from Simple_Cypher_Decrypt import decrypt

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