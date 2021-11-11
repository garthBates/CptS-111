######################
#Garth Bates
#CptS 11, Spring 2018
#Programming Assignment #5
#3/20/2018
#gold_ratio.py
#Calculates and prints the Fibonacci sequence for a user submitted number of values
######################

def fib(terms):
    """Takes a single integers eual to or greater than 1 and prints the number of elements in the Fibonacci sequence eual to that"""
    if (terms < 1):  #verifies of user input is a valid input
        print("Invalid number")
        main()
    else:
        first = 1 #initializing to 1
        print("1 ", first) #prints first line of output
        second = 1 #initializing to 1

        for i in range(terms - 1): #Calculated Fibonacci sequence
            print(i + 2," ", end = "") #prints number in sequence
            print(second, end = "") #prints value of current element
            gold_ratio = (second / first) #calulated the golden ration for current element
            print(" ", gold_ratio) #prints golden ratio
            third = first + second #creates next element in sequence
            first = second #resets values to properly run the loop again
            second = third

def main():
    """Main function gets the user input for number of terms in the Fibonacci sequance and runs the fib function"""
    num_terms = int(input("Enter the number of terms you want to find: ")) #Gets the user desired number of terms for Fibonacci sequence
    fib(num_terms) #runs fib funcion with user desired number of terms

main()
