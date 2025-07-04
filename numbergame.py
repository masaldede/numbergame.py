#number guess game
# fix counter

import random
while True:
    menu="""
     _____________________________________________
    |                Welcome Player               |
    |    I choose the number between 1 to 20      |
    |_____________________________________________|"""
    print(menu)

    mynumber = random.randint (1,20)
    guess = int(input("Make a guess:"))
    counter=0

    def game(guess):

        while guess != mynumber:

            if guess > mynumber:
                print(guess, " is bigger than my number")
                guess = int(input("Make a new guess:"))

            elif guess < mynumber:
                print(guess, " is lower than my number")
                guess = int(input("Make a new guess:"))

    game(guess)

    print("CORRECT!", mynumber, " is my number!")
    print ("you tried ",counter," times!")
    print("Type 1 to play again, type any other number to exit")


    again = int(input("Your choice:"))
    if again == 1:
        print ("New game selected. ENJOY!")
        continue
    else:
        print("Exit selected. See you later!")
        break
