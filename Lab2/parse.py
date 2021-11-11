#Garth Bates
#1/24/2018
#CptS 111
#Lab #2, Task 1


      
user_int = int(input("Please enter a positive four-digit integer: "))

digit1 = user_int // 1000
print(digit1)
digit2 = (user_int // 100) % 10
print(digit2)
digit3 = (user_int // 10) % 10
print(digit3)
digit4 = user_int % 10
print(digit4)
