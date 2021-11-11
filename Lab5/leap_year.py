#########
#Garth Bates
#Lab 5, task 2
#2/14/2018
#########

def leap_year(year):
    if (year % 100 == 0):
        if (year % 400 == 0):
            return True
        else:
            return False
    if (year % 4 == 0):
        return True
    else:
        return False

def main():
    year = int(input("Please enter a year: "))
    test = leap_year(year)
    if (test == True):
        print(year, "is a leap year!")
    else:
        print(year, "isn't a leap year.")

main()
