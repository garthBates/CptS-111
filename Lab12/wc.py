import os
os.chdir("D:/CS 111/Lab12")

filename = "poem.txt"
file = open(filename, "r")

def wc(file):
    fstring = file.read()
    lines = fstring.count("\n")
    #print(lines)
    chars = len(fstring)
    #print(chars)
    fstring = fstring.replace("\n", " ")
    words = fstring.split(" ")
    #print(words)
    words = (len(words) - 1)
    print("\t", lines, "\t", words, "\t", chars, " ", filename, sep = "")


wc(file)
