

#init
import random
wins = 0
losses = 0
ties = 0
#function

#main
#step 1
def game():
    global wins
    global losses
    global ties
    print("Make your move")
    player = input("Rock, Paper, scissors")
    #step 2: Generate a move for the computer
    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
        print("the computer's move is rock")
    if computer == 2:
        computer = "paper"
        print("the computer's move is paper")
    if computer == 3:
        computer = "scissors"
        print("the computer's move is scissors")

    #step 3: Determine the outcome
    if player == "rock" and computer == "rock":
        print("it is a tie")
        ties = ties + 1
        print (("tie score: ") + str(ties))
    elif player == "rock" and computer == "paper":
        print("you lose")
        losses = losses + 1
        print (("losses score: ") + str(losses))
    elif player == "rock" and computer == "scissors":
        print("you win")
        wins = wins + 1
        print(("wins score: ") + str(wins))
    elif player == "paper" and computer == "rock":
        print("you win")
        wins = wins + 1
        print(("wins score: ") + str(wins))
    elif player == "paper" and computer == "paper":
        print("tie")
        ties = ties + 1
        print (("tie score: ") + str(ties))
    elif player == "paper" and computer == "scissors":
        print("you lose")
        losses = losses + 1
        print (("losses score: ") + str(losses))
    elif player == "scissors" and computer == "rock":
        print("you lose")
        losses = losses + 1
        print (("losses score: ") + str(losses))
    elif player == "scissors" and computer == "paper":
        print("you win")
        wins = wins + 1
        print(("wins score: ") + str(wins))
    elif player == "scissors" and computer == "scissors":
        print("ties")
        ties = ties + 1
        print (("tie score: ") + str(ties))

    #step 4: loop

    while True:
            #step 1
            print("Make your move")
            player = input("Rock, Paper, scissors")


            #step 2: Generate a move for the computer
            computer = random.randint(1,3)
            if computer == 1:
                computer = "rock"
                print("the computer's move is rock")
            if computer == 2:
                computer = "paper"
                print("the computer's move is paper")
            if computer == 3:
                computer = "scissors"
                print("the computer's move is scissors")

            #step 3: Determine the outcome
            if player == "rock" and computer == "rock":
                print("it is a tie")
                ties = ties + 1
                print (("tie score: ") + str(ties))
            elif player == "rock" and computer == "paper":
                print("you lose")
                losses = losses + 1
                print (("losses score: ") + str(losses))
            elif player == "rock" and computer == "scissors":
                print("you win")
                wins = wins + 1
                print(("wins score: ") + str(wins))
            elif player == "paper" and computer == "rock":
                print("you win")
                wins = wins + 1
                print(("wins score: ") + str(wins))
            elif player == "paper" and computer == "paper":
                print("tie")
                ties = ties + 1
                print (("tie score: ") + str(ties))
            elif player == "paper" and computer == "scissors":
                print("you lose")
                losses = losses + 1
                print (("losses score: ") + str(losses))
            elif player == "scissors" and computer == "rock":
                print("you lose")
                losses = losses + 1
                print (("losses score: ") + str(losses))
            elif player == "scissors" and computer == "paper":
                print("you win")
                wins = wins + 1
                print(("wins score: ") + str(wins))
            elif player == "scissors" and computer == "scissors":
                print("ties")
                ties = ties + 1
                print (("tie score: ") + str(ties))


            playagain = input("would you like to play")
            if playagain.lower() == "yes":
                    print("restarting..")
            else:
                    print("Thanks for playing")
                    break

game()




