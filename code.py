import random
# computerSelection = ""
# playerSelection = ""
# options = "rock", "paper", "scissors"
computerWin = 0
playerWin = 0
# number = 0
# winnerPlayer = 0

def game():
    global playerWin
    global computerWin
    playerSelection = str(input("Type your selection: "))
    computerSelection = random.randint(0, 2)
    if computerSelection == 0:
        computerSelection = "rock"
    elif computerSelection == 1:
        computerSelection = "paper"
    elif computerSelection == 2:
        computerSelection = "scissors"

    if playerSelection == "rock":
        playRound("rock", computerSelection)
    elif playerSelection == "paper":
        playRound("paper", computerSelection)
    elif playerSelection == "scissors":
        playRound("scissors", computerSelection)
    else:
        print("nothing")

def playRound(a, b):
    # global winnerPlayer
    global playerWin
    global computerWin
    # computerWin = 0
    # playerWin = 0
    # winnerPlayer = 0
    while True:
        if playerWin != 5 and computerWin != 5:
            print(f"Computer selects {b}")
            print(f"You select {a}")
            if a == "rock" and b == "scissors":
                # playerWin += 1
                playerWin += 1
                print("You win!")
                print(f"Player wins: {playerWin}")
                print(f"Computer wins: {computerWin}")
                game()
            elif a == "paper" and b == "rock":
                # playerWin += 1
                playerWin += 1
                print("You win!")
                print(f"Player wins: {playerWin}")
                print(f"Computer wins: {computerWin}")
                game()
            elif a == "scissors" and b == "paper":
                # playerWin += 1
                playerWin += 1
                print("You win!")
                print(f"Player wins: {playerWin}")
                print(f"Computer wins: {computerWin}")
                game()
            elif a == b:
                print("Tie game!")
                print(f"Player wins: {playerWin}")
                print(f"Computer wins: {computerWin}")
                game()
            else:
                computerWin += 1
                print("Computer wins!")
                print(f"Player wins: {playerWin}")
                print(f"Computer wins: {computerWin}")
                game()
            continue
    if playerWin == 5:
        print("You win!!")
    else:
        print("Computer wins!!")
        


# playerSelection = str(input("Type your selection: "))
# game(playerSelection)
game()

#hey its alex!

