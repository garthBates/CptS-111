############
#Garth Bates
#CS 111
#Lab 4, task 3
#2/7/2018
############


def sum_digits(user_int):
    digit1 = user_int // 10000
    digit2 = (user_int // 1000) % 10
    digit3 = (user_int // 100) % 10
    digit4 = (user_int // 10) % 10
    digit5 = user_int % 10
    total = digit1 + digit2 + digit3 + digit4+ digit5
    return total
    
def main():
    user_int = int(input("Enter an integer up to five digits: "))
    total = sum_digits(user_int)
    print("The sum of the digits in ", user_int, ": ", total, sep="")
    total = sum_digits(total)
    print("The sum of the digits in ", total, ": ", total, sep="")
    
    

main()
