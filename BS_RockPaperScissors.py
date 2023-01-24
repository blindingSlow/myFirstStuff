# import libraries
import random, os, time

# String animation
def animaString(string):
    name = string
    nameLength = len(name)
    roll = 0
    while roll <=nameLength :
        os.system("clear")
        print(name[:roll])
        roll += 1
        time.sleep(.05)

# call intro animation
animaString("Blinding Slow Artsy Stuff kinda proudly presents:")

# main game function
def startGame() :

# set initial score
    pOneScore = 0
    pTwoScore = 0

# "tutorial"    
    print("""
Rock, Paper, Scissors...
-------------------------------------
Type a number and press Enter/Return
1 = Rock
2 = Paper
3 = Scissors      
-------------------------------------
    """)

# set hands list
    handList = ("Rock", "Paper", "Scissors")

# validate player choice
    while pOneScore < 3  and pTwoScore < 3:
        pOnePick = input("Choose your hand: ")
        while pOnePick != "1" and pOnePick != "2" and pOnePick != "3" :
                print()
                print("Invalid option! Use 1 for rock, 2 for paper or 3 for scissors.")
                pOnePick = input("Go: ")
                continue

# select hand option from list
        if pOnePick == "1" :
            pOnePick = handList[0]
        elif pOnePick == "2" :
            pOnePick = handList[1]
        elif pOnePick == "3" :
            pOnePick = handList[2]

# pick a random option from list for the computer hand
        pTwoPick = random.choice(handList)

# clear screen and print picked hands to the console
        print()
        os.system("clear")
        print(f"Your hand:      {pOnePick}")
        print(f"Computer hand:  {pTwoPick}")

# set the game winner and increase score
        winner = ""
        if pOnePick == pTwoPick :
            winner = "Draw"
        if pOnePick == "Rock" :
            if pTwoPick == "Paper" :
                pTwoScore += 1
                winner = "Computer"
            if pTwoPick == "Scissors" :
                pOneScore += 1
                winner = "Player"
        if pOnePick == "Paper" :
            if pTwoPick == "Scissors" :
                pTwoScore += 1
                winner = "Computer"
            if pTwoPick == "Rock" :
                pOneScore += 1
                winner = "Player"
        if pOnePick == "Scissors" :
            if pTwoPick == "Rock" :
                pTwoScore += 1
                winner = "Computer"
            if pTwoPick == "Paper" :
                pOneScore += 1
                winner = "Player"

# get game winner and print it to the console
        print()
        if winner == "Player" :
            print("You won!")
        elif winner == "Computer" :
            print("Computer won!")
        elif winner == "Draw" :
            print("It's a draw!")
        
# print the new score
        print()
        print(f"""Match Score (Best of 3):
You:       {pOneScore}
Computer:  {pTwoScore}""")
        print()

# check if there is a match winner        
        if pOneScore == 3 :
            print()
            print("You are the match winner!!!")
        if pTwoScore == 3 :
            print()
            print("Computer is the match winner!")

# reset or quit function        
    def again() :

# get and validate player choice        
        print()
        resetGame = input("Play again! Yes or No?")
        while resetGame != "y" and resetGame != "n" :
            print("Invalid option! Use 'y' for YES or 'n' for NO")
            resetGame = input("Let's play again? ")
            continue

# if YES, clear screen and reset game
        if resetGame == "y" :
            os.system("clear")
            startGame()

# if NO, print animated quiting messages and exit game
        if resetGame == "n" :
            animaString("""Blinding Slow Artsy Stuff kinda thank you for playing...
...seriously though, thanks!""")
            time.sleep(1)
            animaString("contact me! github.com/blindingslow")
            time.sleep(5)
            animaString("Goodbye!!!")
            time.sleep(2)
            os.system("clear")
            exit()

# call reset or quit function
    again()

# call main game function
startGame()
