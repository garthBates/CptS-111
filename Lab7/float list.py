#Garth Bates
#2/28/2018
#Cpts 111
#Lab #7, Task 4

def get_floats(user_int):
    floats = []
    for i in range(user_int):
        print("Enter float", i + 1, ":", end = " ")
        new_float = float(input())
        floats.append(new_float)
    #print(floats)
    return floats
    
def main():
        user_int = int(input("Enter the number of list elements: "))
        floats = []
        floats = get_floats(user_int)
        print(floats)
        

main()
