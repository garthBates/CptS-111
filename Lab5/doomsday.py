#########
#Garth Bates
#Lab 5, task 3
#2/14/2018
#########

def calc_doom(year, anchor):
    doomsday = (((year // 12) + (year % 12) + (year % 12) // 4) % 7 + anchor) % 7
    print("\nDoomsday =", doomsday)
    
def set_anchor(cent):
    if (cent == 19):
        return 3
    elif (cent == 20):
        return 2
    else:
        print("Year invalid")

def main():
    year = int(input("Enter the year in four digits [1900 - 2099]: "))
    cent = year // 100
    year = year % 100
    anchor = set_anchor(cent)
    calc_doom(year, anchor)

main()
