####
#Lab 3 task 2
#

def calc_doom(year, anchor):
    doomsday = (((year // 12) + (year % 12) + (year % 12) // 4) % 7 + anchor) % 7
    print("\nDoomsday =", doomsday)


year = int(input("Enter the last two digits of the year: "))
anchor = int(input("Enter the anchor day as an integer [0=Sunday, 7=Saturday]: "))

calc_doom(year, anchor)
