######################
#Garth Bates
#CptS 11, Spring 2018
#Programming Assignment #5
#3/20/2018
#stats.py
#Finds the average and the standard deviation of a user submitted list of numbers
######################

import math as m

def get_floats(user_int):
    """Gets the inputs for the user created list and returns the list"""
    floats = []  #initializing the float list
    for i in range(user_int): #appending the desired values to the list
        print("Enter float", i + 1, ":", end = " ")
        new_float = float(input())
        floats.append(new_float)
    return floats #returns the completed list

def summer(float_list):
    """Adds all the values of the list together and returns the sum"""
    accum = 0 #initializing the accumlator
    for i in range(len(float_list)): #add all the values of the list by using augmented notation adn the accumulator
        x = float_list[i]
        accum += x
    return accum #returns the sum of all list values
    

def average(floats):
    """Averages all the values of the user created list and returns the average"""
    return (summer(floats) / len(floats)) #Calculated the average of all list a=values and returns it


def std_dev(floats, average):
    """Calcualtes the standard deviation for the user created list and returns its value"""
    accum = 0 #initializing the accumulator
    for i in range(len(floats)): #subtracs the average from all values in list
        x = floats[i] - average
        accum += x**2            #then squares the difference and add it to the accumulator
    y = accum / len(floats)  #divides the accumulator by the number of elements in the list
    dev = m.sqrt(y) #gets the square root of that value
    return dev #returns the standard deviation

def main():
    """Main function where user enters the ammount of elements in list and then prints the values for the average adn standard deviation"""
    user_int = int(input("Enter the number of list elements: ")) #Gets the amount of elements in the list
    floats = get_floats(user_int) #runs get_floats funcation and saves return value to floats
    avg = average(floats) #runs average function and saves retrned value to avg
    dev = std_dev(floats, avg) #runs std_dev function and saved returned value to dev
    print("Average =", avg) #prints the average value
    print("Standard Deviation =", round(dev, 2)) #prints the standard deviation rounded two decimal places

main()
