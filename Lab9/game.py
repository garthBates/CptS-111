from random import *

def guessing_game():
    num_players = int(input("Enter number of players: "))
    target_number = randrange(1, 101)
    print("I'm thinking of a number between 1 and 100. Guess what it is.")

    player = 0

    for i in range(101):
        #player = (player + 1) % num_players       
        prompt = "Player " + str(player +1) + "? "
        print(prompt, end = "")
        guess = int(input())
        if guess < target_number:
            print("Too low")
        elif guess > target_number:
            print("Too high")
        else:
            print("***PLAYER " + str(player + 1) + " WINS!***")
            break
        player = (player + 1) % num_players  

guessing_game()

        
