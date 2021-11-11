#Garth Bates
#1/17/2018
#Cpts 111
#Lab #1, Task 5

hours = int(input("Enter the number of elapsed hours: "))
minutes = int(input("Enter the number of elapsed minutes: "))
seconds = int(input("Enter the number of elapsed seconds: "))

print()

total_seconds = hours * 3600 + minutes * 60 + seconds
print("The total number of elapsed seconds: ", total_seconds)

total_hours = hours + minutes / 60 + seconds / 3600
print("The total number of elapsed hours: ", total_hours)
