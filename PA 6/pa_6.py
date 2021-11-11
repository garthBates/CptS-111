######################
#Garth Bates
#CptS 11, Spring 2018
#Programming Assignment #6
#4/82018
#benford.py
#Tests the legitmacy of data from an imported file using Benford's theory
######################

#imports the provided show_digits function 
from show_digits import *


def main():
    """Initialzes all lists. Reads desired file and exratpilates the usable data.
    Tallies number of leading digit occurances, then runs them through show_digits function"""
    
    tally = [0] * 9 #initializes tallies

    data = [] #initialzes data
    
    file = open(input("Enter filename: "), "r") #opens desired file for reading
    for line in file: #gets usable data points from file and appends them to data list
        dataln = str(line)
        dataln = dataln.split(",")
        datapt = dataln[-1]
        datapt = datapt.strip()
        data.append(datapt)
            
    for datapt in data: #gets the first digit from data point and increments the appropriate tally
        lead = datapt[0]
        lead = int(lead)
        tally[lead - 1] += 1
        
    show_digits(tally)
    print(tally)
            
main()

