#Garth Bates
#1/24/2018
#CptS 111
#Lab #2, Task 5

year = int(input("Enter the last two digits of the year: "))
anchor = int(input("Enter the anchor day as an integer [0=Sunday, 7=Saturday]: "))


doomsday = (((year // 12) + (year % 12) + (year % 12) // 4) % 7 + anchor) % 7

print("\nDoomsday =", doomsday)


