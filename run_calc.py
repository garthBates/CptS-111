################
#Garth Bates
#CptS 111, Spring 2018
#Programming Assignment #3
#2/9/2018
#Running Time Calculator
#A calculator that given a pace and distance can calculate the time to run said distance
#Else if and elif tutorial https://www.tutorialspoint.com/python/python_if_else.htm
################

def get_input():
    """Gets the inputs of pace and distance from the user, then converts them into usable data types"""
    pace = str(input("Enter pace [mm:ss]: "))  #Gets the user input for pace
    mm, ss = int(pace.split(":") [0]), int(pace.split(":")[1])
    sec_per_mile = (mm * 60) + ss #converts the pace into usable data
    dist = float(input("Enter distance [miles]: ")) #Gets user input for distance
    calc_time(sec_per_mile, dist)

def calc_time(sec_per_mile, dist):
    """calculates the total time, in seconds, for the pace and distance"""
    total_time = sec_per_mile * dist #calculates the total time to run based of seconds and distance
    total_time = int(total_time) #converts total time into usable data
    print()
    display_time(total_time)

def display_time(total_time):
    """Displays the total time in the form (hh:mm:ss)"""
    hours = total_time // 3600 #gets the total hours
    minutes = ((total_time % 3600) // 60) #gets the total minutes
    seconds = total_time -((hours * 3600) + (minutes * 60)) #gets the total seconds
    if (seconds < 10 and minutes < 10): #properly prints the time in the standard format (hh:mm:ss)
        print(hours, ":0", minutes, ":0", seconds, sep="")
    elif (minutes < 10):
        print(hours, ":0", minutes, ":", seconds, sep="")
    elif (seconds < 10):
        print(hours, ":", minutes, ":0", seconds, sep="")
    else:
        print(hours, ":", minutes, ":", seconds, sep="")

def main():
    """the Main function that runs the program"""
    get_input()
    
    
main()
