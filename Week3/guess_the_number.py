import simplegui
import random

# The key idea of this program is using binary search 
# to find the secret number.

# global variables
secret_num = 0	
n = 7
current_guess = 0
new_range = 99

# helper function to start and restart the game
def new_game():
    """
    Resets current guess number current guess to 0.
    """    
    global current_guess
    current_guess = 0
    
# define event handlers for control panel
def range100():
    """
    Starts a new game, with a range of [0, 100).
    """
    global n, secret_num, new_range
    n = 7
    secret_num = random.randrange(0, 100)
    new_range = 99
    print "Guess a number between 0-99 in " + str(n) + " guesses. Good luck!\n"
    return new_game()
    
def range1000():
    """
    Starts a new game, with a range of [0, 1000).
    """
    global n, secret_num, new_range
    n = 10
    secret_num = random.randrange(0, 1000)
    new_range = 999
    print "Guess a number between 0-999 in " + str(n) + " guesses. Good luck!\n"    
    return new_game()
    
def input_guess(guess):
    """
    Converts the string guess to an integer, and compares it with the secret number secret_num.
    """
    global current_guess 
    # Converts guess to integer.
    guess_int = int(guess)
    print "You guessed " + str(guess_int) + "."
    
    # Compares guess to secret_num.
    if guess_int > new_range:
        print "Guess a number between 0-" + str(new_range) + "! Make sure you are within the limit!\n"  
    else:
        # Increments global variable current_guess.
        current_guess += 1
        remaining_guesses = n - current_guess
        
        if (remaining_guesses == 0) and (guess_int != secret_num):
            print "Game over! Secret number was " + str(secret_num) + "."
            new_game()
        elif guess_int < secret_num:
            print "Higher!"
            print str(remaining_guesses) + " guess(es) left.\n"

        elif guess_int > secret_num:
            print "Lower!"
            print str(remaining_guesses) + " guess(es) left.\n"

        else:
            print "Correct! Secret number was " + str(secret_num) + ".\n"
            new_game()
            
    
# create frame
frame = simplegui.create_frame("Guess the number game", 300, 300)

# register event handlers for control elements and start frame
button1 = frame.add_button("Start a new game with the range [0 100)", range100, 200)
button2 = frame.add_button("Start a new game with the range [0 1000)", range1000, 200)                        
input = frame.add_input("Enter Guess", input_guess, 100)

# call new_game 
new_game()
