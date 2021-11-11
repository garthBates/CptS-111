def shrink(user_string, lines):
    for i in range(lines):
        lines -= 1
        for j in range(len(user_string)):
            print(user_string[j] + " " * lines, end = "")
        print()
        

def main():
    user_string = input("Enter string: ")
    lines = int(input("Enter number of lines: "))

    shrink(user_string, lines)

main()
