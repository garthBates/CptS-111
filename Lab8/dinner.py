############
#Garth Bates
#3/7/2018
#CptS 111
#Dinner
############



def selection(prompt, num_choice):
	choices = []
	for i in range(num_choice):
		options = []
		dish = input(prompt)
		options.append(dish)
		options.append(0)
		choices.append(options)
	return choices

def menu(choices):
        food = ""
        for i in range(len(choices) - 1):
                food += str(i +1) + ") " +choices[i][0] + ", "
        food += str(len(choices)) + ") " + choices[-1][0] + ": "
        print(food, end = "")

def choose(choices):
        thingy = menu(choices)
        pick = int(input())
        choices[pick - 1][1] += 1

def report(entrees, drinks, desserts, num_entrees, num_drinks, num_desserts):
        print("***DINNER PARTY ORDERS***")
        print()
        print("The entree orders are as follows:")
        for i in range(num_entrees):
                print("\t", entrees[i][0], ":", entrees[i][1])

        print("The dessert orders are as follows:")
        for i in range(num_drinks):
                print("\t", desserts[i][0], ":", desserts[i][1])

        print("The drink orders are as follows:")
        for i in range(num_desserts):
                print("\t", drinks[i][0], ":", drinks[i][1])

def main():

        guests = int(input("How many guests will be attending: "))
        num_entrees = int(input("How many entress options will there be: "))
        num_drinks = int(input("How many drink options will there be: "))
        num_desserts = int(input("How many dessert options will there be: "))

        
        entrees = selection("Enter an entree option: ", num_entrees)
        drinks = selection("Enter a drink option: ", num_drinks)
        desserts = selection("Enter a dressert option: ", num_desserts)

        for i in range(guests):
                print("Guest #", i + 1, ":", sep = "")
                choose(entrees)
                choose(drinks)
                choose(desserts)

        report(entrees, drinks, desserts, num_entrees, num_drinks, num_desserts)
        
        
        
main()
