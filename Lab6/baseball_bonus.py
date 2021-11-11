#Garth Bates
#2/21/2018
#Cpts 111
#Lab #6, Task 2

def main():
    print("For each of the following, enter y for yes, and n for no.")
    all_star = input("All-Star Game appearance? ")
    reg_mvp = input("Regular season MVP? ")
    world_mvp = input("World Series MVP? ")
    gg = input("Gold Glove award? ")
    ss= input("Silver Slugger award? ")
    home = input("Home run champ? ")
    batting = input("Batting average champ? ")

    bonus = 0

    if (all_star == "y"):
        bonus = bonus + 25000
    if (reg_mvp == "y"):
        bonus = bonus + 75000
    if (world_mvp == "y"):
        bonus = bonus + 100000
    if (gg == "y"):
        bonus = bonus + 50000
    if (ss == "y"):
        bonus = bonus + 35000
    if (home == "y"):
        bonus = bonus + 25000
    if (batting == "y"):
        bonus = bonus + 25000

    print("This baseball player's bonus was $", bonus, ".", sep ="")

main()

    

    
        
