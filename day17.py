from getpass import getpass as input
counter = 0
scorep1 = 0
scorep2 = 0
while True:
    print("Select your move (R-rock 👊, P-paper 📄, S-scissor ✂)")
    player1 = str(input("Player 1 enter a choice (R or P or S): ").upper())
    print("Select your move (R-rock 👊, P-paper 📄, S-scissor ✂)")
    player2 = str(input("Player 2 enter a choice (R or P or S): ").upper())
    print("R-👊 P-📄 S-✂")
    print("Player 1: ", player1)
    print("Player 2: ", player2)
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "R" and player2 == "S":
        print("Player 1's Rock win!")
        scorep1 +=1
    elif player1 == "P" and player2 == "R":
        print("Player 1's Paper win!")
        scorep1 +=1
    elif player1 == "S" and player2 == "P":
        print("Player 1's Scissors win!")
        scorep1 +=1
    else:
        print("Player 2 win!")
        scorep2 +=1
    counter +=1
    if scorep1 ==3 or scorep2 ==3:
        break
    else:
        continue
print("The game is over in ", counter, "games")
if scorep1 > scorep2:
    print("Player 1 wins!!")
else:
    print("Player 2 wins!!")