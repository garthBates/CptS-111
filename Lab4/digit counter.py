############
#Garth Bates
#CS 111
#Lab 4, task 1
#2/7/2018
############


def calculate (j, k):
    number = j ** k
    digits = len(str(number))
    print(j, "**", k, "=", number)
    print("This number has", digits, "numbers in it.")

def main():
    j = int(input("Enter the base j: "))
    k = int(input("Enter the exponent k: "))
    calculate(j, k)

main()
