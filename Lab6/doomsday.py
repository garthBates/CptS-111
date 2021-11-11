#########
#Garth Bates
#Lab 6, task 5
#2/21/2018
#########

def calc_doom(year, anchor):
    doomsday = (((year // 12) + (year % 12) + (year % 12) // 4) % 7 + anchor) % 7
    print("\nDoomsday =", doomsday)
    return doomsday
    
def set_anchor(cent):
    if (cent == 19):
        return 3
    elif (cent == 20):
        return 2
    else:
        print("Year invalid")
        
def get_day(doomsday):
    if (doomsday == 0):
        return "Sunday"
    elif (doomsday == 1):
        return "Monday"
    elif (doomsday == 2):
        return "Tuesday"
    elif (doomsday == 3):
        return "Wednesday"
    elif (doomsday == 4):
        return "Thursday"
    elif (doomsday == 5):
        return "Friday"
    elif (doomsday == 6):
        return "Saturday"
    
def main():
    year = int(input("Enter the year in four digits [1900 - 2099]: "))
    cent = year // 100
    year = year % 100
    anchor = set_anchor(cent)
    doomsday = calc_doom(year, anchor)
    day = get_day(doomsday)
    print("Doomsday:", day)

main()
