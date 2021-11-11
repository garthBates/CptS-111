from math import *

def main():
    user_func = input("Enter f(x): ")
    user_x = float(input("Enter a value of x: "))

    x = user_x

    answer = eval(user_func)

    print()
    print("f(x) =", user_func)
    print("f(", user_x, ") = ", answer, sep="")

main()
