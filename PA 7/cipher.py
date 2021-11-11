# John B. Schneider
# gen_amp_seed() function
#######################################################################
# Function to calculate an "amplitude" and a "seed" appropriate for
# starting the encryption/decryption process.  These values are based
# on the password given as the argument (which is assumed to be a
# string).  This function uses the SHA1 hash function from the hashlib
# module.  See http://en.wikipedia.org/wiki/SHA-1 for details
# concerning this function.  The hash function creates a unique
# 160-bit 'digest' for a given string.  This digest is split into two
# parts.  One part is used to set the amplitude and the other is used
# to set the seed value.
import hashlib

def gen_amp_seed(password):
    h = hashlib.sha1()          # Create a SHA1 hash object.
    h.update(password.encode()) # Update object with password.
    # Create a 160-bit hexadecimal digest which is returned as a
    # 40-character string.
    d = h.hexdigest()
    # Split the digest into two parts, each of 20 hexadecimal
    # characters/digits.
    d1 = d[ : 20]     
    d2 = d[20 : ]
    # max_possible is the maximum possible value that 20 hexadecimal
    # digits can have.
    max_possible = 0xFFFFFFFFFFFFFFFFFFFF
    # Set the amp and seed values.  amp is 3.99 plus a number that is
    # between 0.0 and 0.01 while seed is between 0.0 and 1.0.  In the
    # unlikely event that d2 equals max_possible, then seed will be
    # 1.0 which will cause the log_map() function to return zero.
    # Although simple to account for this, we will not do so here.
    amp = 3.99 + eval('0x' + d1) / max_possible / 100
    seed = eval('0x' + d2) / max_possible
    return amp, seed


######################
#Garth Bates
#CptS 111, Spring 2018
#Programming Assignment #7
#4/20/2018
#cipher.py
#All funtions written be me for use in encrypt.py and decrpyt.py
# log_map(), cipher_chr(), decipher_chr, line2cipher() functions
#######################################################################

def cipher_chr(text, offset): #ciphers a single character
    x = ord(text) - 32
    x += offset
    x = x % 95
    x += 32
    x = chr(x)
    return x

def decipher_chr(text, offset): #deciphers a single character
    x = ord(text) - 32
    x -= offset
    x = x % 95
    x += 32
    x = chr(x)
    return x

def log_map(amp, cur_gen): #used in generating seeds
    return (amp * cur_gen * (1 - cur_gen))

def line2cipher(amp, seed, clear): #ciphers one line of text
    accum = ""
    for i in range(len(clear)):
        seed = log_map(amp, seed)
        offset = int(seed * 96)
        x = clear[i]
        x = cipher_chr(x, offset)
        accum = accum + x
    return amp, seed, accum

def line2clear(amp, seed, cipher): #deciphers one line of text
    accum = ""
    for i in range(len(cipher)):
        seed = log_map(amp, seed)
        offset = int(seed * 96)
        x = cipher[i]
        x = decipher_chr(x, offset)
        accum = accum + x
    return amp, seed, accum

