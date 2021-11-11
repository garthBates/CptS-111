####
#Lab 3 task 5
####

def reverse_digits(user_int):
    digit1 = user_int // 1000
    digit2 = (user_int // 100) % 10
    digit3 = (user_int // 10) % 10
    digit4 = user_int % 10
    print(digit4, digit3, digit2, digit1, sep='')

user_int = int(input("Enter a four-digit positive integer: "))

reverse_digits(user_int)
    
