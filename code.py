computerSelection = ""
playerSelection = ""
options = "rock", "paper", "scissors"
computerWin = 0
playerWin = 0
number = 0

def game(x):
    # computerSelection = idk the python code to get a random number
    if x == "rock":
        playRound("rock", computerSelection)
    elif x == "paper":
        playRound("paper", computerSelection)
    elif x == "scissors":
        playRound("scissors", computerSelection)
    else:
        print("nothing")

def playRound(a, b):
    if playerWin !=5 and computerWin != 5:

        
        print(f"Computer selects {a}")
        print(f"You select {b}")

        if a == "rock" and b == "scissors":
            playerWin += 1
            print("You win!")
            print(f"Player wins: {playerWin}")
            print(f"Computer wins: {computerWin}")
        elif a == "paper" and b == "rock":
            playerWin += 1
            print("You win!")
            print(f"Player wins: {playerWin}")
            print(f"Computer wins: {computerWin}")
        elif a == "scissors" and b == "paper":
            playerWin += 1
            print("You win!")
            print(f"Player wins: {playerWin}")
            print(f"Computer wins: {computerWin}")
        elif a == b:
            print("Tie game!")
            print(f"Player wins: {playerWin}")
            print(f"Computer wins: {computerWin}")


playerSelection == input("Type your selection: ")
game(playerSelection)