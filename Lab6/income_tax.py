#Garth Bates
#2/21/2018
#Cpts 111
#Lab #6, Task 4

def get_rate(income):
    rate = ""
    
    if (income <= 9525):
        rate = "10%"
    elif (income > 9525 and income <= 38700):
        rate = "12%"
    elif (income > 38700 and income <= 82500):
        rate = "22%"
    elif (income > 82500 and income <= 157500):
        rate = "24%"
    elif (income > 157500 and income <= 200000):
        rate = "32%"
    elif (income > 200000 and income <= 500000):
        rate = "35%"
    else:
        rate = "37%"
    print("Your marginal tax rate is", rate)

def main():
    income = int(input("Enter your annual income:"))
    get_rate(income)
        

main()

    

    
        
