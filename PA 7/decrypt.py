######################
#Garth Bates
#CptS 111, Spring 2018
#Programming Assignment #7
#4/20/2018
#dencrpyt.py
#Dencrypts the user designated file
######################

#imports  all nessicary functions from cipher.py
from cipher import *

def main():
    """Main function promts user for password, cipherd file, and decrypted file location"""
    user_pw = input("Enter password: ") #stores user password, must be same as encryption password
    user_cipher = input("Enter cipher text file name: ") #stores file to be decrypted
    user_clear = input("Enter clear text file name: ") #stores out file location
    

    file_in = open(user_cipher, "r")
    file_out = open(user_clear, "w")

    amp, seed = gen_amp_seed(user_pw) #generates seed for decryption based on password

    for line in file_in: #decrypts file
        clean_line = line2clear(amp, seed, line)[2]
        x = len(clean_line)
        print(clean_line[:x-2], file=file_out)


main()
