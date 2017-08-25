'''
This file is a helper class to encrypt and decrypt text.
Its use pycrypto lib and AES-256 CTR mode with 32-byte key that derived from a password.
That key make with "Password-baed key derivation function 2[PBKDF2]"
Author: H.R.Shadhin <hello@hrshadhin.me>
Date: 25-08-2017
'''

import base64
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from fastpbkdf2 import pbkdf2_hmac
import binascii

class MBCryptr:
    '''
    This class help to create key, 
    ciphertext from plaintext and
    plaintext from ciphertext
    '''
    def build_key_from_password(password):
        ''' 
        the password  need to have high entropy, meaning difficult to predict.
        For added #security, i add a "salt", which increases the entropy.
        In this code, i use the RNG to produce the salt that we used to
        produce 32 bytes key. And key is build using pbkdf2 with sha512,8 bytes salt
        '''

        #salt 8 byte size
        salt = b'gshadhin'
        iterations = 10000

        # Stands for "Password-based key derivation function 2"
        hash_bin =pbkdf2_hmac('sha256',password.encode('utf-8'),salt,iterations,16)
        key = binascii.hexlify(hash_bin)

        return key

    # Takes as input a 32-byte key and an arbitrary-length plaintext and returns a
    # ciphtertext.
    def encrypt(key, plaintext):

        # Choose a random, 16-byte IV[initialization vector].
        iv = Random.new().read(AES.block_size)

        #Convert the IV to a Python integer.
        iv_int = int(binascii.hexlify(iv), 16)

        # Create a new Counter object with IV = iv_int.
        ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)

        # Create AES-CTR cipher.
        aes = AES.new(key, AES.MODE_CTR, counter=ctr)

        # Encrypt the text
        ciphertext = aes.encrypt(plaintext)
        #add iv with chiphertext and return
        return base64.b64encode(iv + ciphertext)


    # Takes as input a 32-byte key and a ciphertext, and outputs the
    # corresponding plaintext.
    def decrypt(key, ciphertext):
        #extract iv from ciphertex
        real_cipher = base64.b64decode(ciphertext)
        iv = real_cipher[:16]
        real_cipher_text = real_cipher[16:]
        # # Initialize counter for decryption. iv should be the same as the output of
        # # encrypt().
        iv_int = int(binascii.hexlify(iv), 16)
        ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)

        # Create AES-CTR cipher.
        aes = AES.new(key, AES.MODE_CTR, counter=ctr)

        # Decrypt and return the plaintext.
        plaintext = aes.decrypt(real_cipher_text)
        return plaintext



#test
key = MBCryptr.build_key_from_password('shadhin')
cipher = MBCryptr.encrypt(key,'50000.00')
print(cipher)
plaintext = MBCryptr.decrypt(key,cipher)
print(plaintext)
