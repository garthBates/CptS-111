#Garth Bates
#1/24/2018
#CptS 111
#Lab #2, Task 4

principal = float(input("Enter the amount you owe [no commas]: "))  #gets users principal
rate = float(input("Enter the interest rate [%]: "))    #gets users interest rate
years = float(input("Enter the number of years you want to pay back your loan: "))   #gets the amount of time user has to pay off loan

rate = rate / 100
months = years * 12  #converts the years to pay off loan to months

#does the payment formula
formula_top = (principal * (rate / 12))
formula_bottom1 = (1 + (rate / 12))
formula_bottom = 1 - formula_bottom1 ** -months
payment = formula_top / ( formula_bottom)


total = payment * months
total_interest = total - principal

payment = payment * 100
payment = round(payment)
payment = payment / 100


total = total * 100
total = round(total)
total = total / 100

total_interest = total_interest * 100
total_interest = round(total_interest)
total_interest = total_interest / 100

print("Your monthly payment is $", payment, sep="")
print("The total amount you ended up paying is $", total, sep="")
print("The total amount of interest you paid is $", total_interest, sep="")
      


