######################
#Garth Bates
#CptS 111, Spring 2018
#Programming Assignment #7
#4/20/2018
#encrpyt.py
#Encrypts the user designated file
######################

#imports  all nessicary functions from cipher.py
from cipher import *

def main():
    """Main function promts user for password, file new, and destination for encrypted
    file and save it"""
    user_pw = input("Enter password: ") #stores user password
    user_clear = input("Enter clear text file name: ") #stores file to be encrpyted
    user_cipher = input("Enter cipher text file name: ") #stores out file location

    file_in = open(user_clear, "r")
    file_out = open(user_cipher, "w")

    amp, seed = gen_amp_seed(user_pw) #generates seed for encryption based on password

    for line in file_in: #encrypts file
        print(line2cipher(amp, seed, line)[2], file=file_out)

        
main()

