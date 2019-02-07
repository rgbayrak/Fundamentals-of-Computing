import random as rand

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
"""
This function converts user input string to a number. 
"""
    if name == "rock":
        number = 0

    elif name == "paper":
        number = 1

    elif name == "scissors":
        number = 2

    elif name == "lizard":
        number = 3

    elif name == "Spock":
        number = 4

    else:
        None

    return number

def number_to_name(number):
"""
This function converts number to a possible option string. 
"""
    if number == 0:
        name = "rock"

    elif number == 1:
        name = "paper"

    elif number == 2:
        name = "scissor"

    elif number == 3:
        name = "lizard"

    elif number == 4:
        name = "Spock"

    else:
        None

    return name


def rpsls(player_choice):
"""
This function takes player input, random chooses computer input and decides who win the game.
"""
    print("")

    if player_choice == "rock":
        print ("Player chooses " + player_choice)
        player_number = name_to_number(player_choice)

    elif player_choice == "paper":
        print("Player chooses " + player_choice)
        player_number = name_to_number(player_choice)

    elif player_choice == "scissors":
        print("Player chooses " + player_choice)
        player_number = name_to_number(player_choice)

    elif player_choice == "lizard":
        print("Player chooses " + player_choice)
        player_number = name_to_number(player_choice)

    elif player_choice == "Spock":
        print("Player chooses " + player_choice)
        player_number = name_to_number(player_choice)

    else:
        None

    computer_guess = rand.randrange(0, 5)
    comp_choice = number_to_name(computer_guess)
    print("Computer chooses " + comp_choice)

    outcome = (player_number - computer_guess) % 5

    if outcome == 0:
        print("Player and computer tie!")

    elif outcome == 1:
        print("Player wins!")

    elif outcome == 2:
        print("Player wins!")

    elif outcome == 3:
        print("Computer wins!")

    elif outcome == 4:
        print("Computer wins!")

    return None

#test 
rpsls("rock")
