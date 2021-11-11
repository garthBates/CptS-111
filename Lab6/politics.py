#Garth Bates
#2/21/2018
#Cpts 111
#Lab #6, Task 3

def run4senate(age, cit):
    if (age >= 30 and cit >= 9):
        print("You're eligible to run for the Senate")
    else:
        print("You're not eligible to run for the Senate")


def run4house(age, cit):
    if (age >= 25 and cit >= 7):
        print("You're eligbile to run for the House of Representitives")
    else:
        print("You're not eligible to run for th House of Representatives")

def main():
    age = int(input("Enter your age in years: "))
    cit = int(input("Enter the number of year you have been a US citizen: "))

    run4senate(age, cit)
    run4house(age, cit)

main()

    

    
        
