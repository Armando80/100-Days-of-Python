from getpass import getpass as input
"""con la línea anterior evitamos que el otro jugador vea la respuesta del otro /
with the previous line we prevent the other player from seeing the other player's answer"""
import os
clear = lambda: os.system('cls')
"""con las 2 lineas anteriores importamos la funcion clear para borrar la consola /
With the two previous lines we import the clear function to clear the console"""
print("Select your move (R-rock 👊, P-paper 📄, S-scissor ✂)")
player1 = str(input("Player 1 enter a choice (R or P or S): ").upper())
clear()
print("Select your move (R-rock 👊, P-paper 📄, S-scissor ✂)")
player2 = str(input("Player 2 enter a choice (R or P or S): ").upper())
clear()
print("R-👊 P-📄 S-✂")
print("Player 1: ", player1)
print("Player 2: ", player2)
if player1 == player2:
    print("It's a tie!")
elif player1 == "R" and player2 == "S":
    print("Player 1's Rock win!")
elif player1 == "P" and player2 == "R":
    print("Player 1's Paper win!")
elif player1 == "S" and player2 == "P":
    print("Player 1's Scissors win!")
else:
    print("Player 2 win!")