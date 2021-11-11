################
#Garth Bates
#CptS 111, Spring 2018
#Programming Assignment #4
#3/1/2018
#Car Service Invoice
################


def print_menu():
    print("Zooey's (College Fund) Car Shop Services:")
    print("Oil change -- $35")
    print("Tire rotation -- $19")
    print("Car wash -- $7")
    print("Car wax -- $12")
    print()

def select_svc():
    svc1 = input("Select first service:\n")
    svc2 = input("Select second service:\n")
    print()
    return svc1, svc2

def make_invoice(svc1, svc2):
    total = 0

    print()
    print(40 * "=")
    print()
    print("Zooey's (College Fund) Car Shop Invoice")
    print()

    if (svc1 == "Oil change"):
        print("Service 1: Oil change, $35")
        total += 35
    if (svc1 == "Tire rotation"):
        print("Service 1: Tire rotation, $19")
        total += 19
    if (svc1 == "Car wash"):
        print("Service 1: Car wash, $7")
        total += 7
    if (svc1 == "Car wax"):
        print("Service 1: Car wax, $12")
        total += 12
    if (svc1 == "-"):
        print("Service 1: No service")

    if (svc2 == "Oil change"):
        print("Service 2: Oil change, $35")
        total += 35
    if (svc2 == "Tire rotation"):
        print("Service 2: Tire rotation, $19")
        total += 19
    if (svc2 == "Car wash"):
        print("Service 2: Car wash, $7")
        total += 7
    if (svc2 == "Car wax"):
        print("Service 2: Car wax, $12")
        total += 12
    if (svc2 == "-"):
        print("Service 2: No service")

    print()
    print("Total: $", total, sep = "")


def main():

    print_menu()
    svc1, svc2 = select_svc()
    make_invoice(svc1, svc2)

main()
