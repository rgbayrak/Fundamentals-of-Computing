# implementation of card game - Memory
#
# The objective of this programming assignment is  
# practicing mouse input/control, lists/dictionaries
#
# Independent Study (Week6)
# Roza Gunes Bayrak
# Vanderbilt University

# struggled with the logic, of how to transfer information between 
# methods without using global variables

import simplegui
import random

global deck, frameX, frameY, state, exp_cards, turns
deck = range(8)
deck2 = range(8)
deck.extend(deck2)
frameX = 800
frameY = 100
state = 0
turns = 0
exp_cards = []


# helper function to initialize globals
# 
#
def new_game():
    global exp_cards, deck, state, turns
    random.shuffle(deck) # with the new game shuffle the deck
    exp_cards = []
    state = 0
    label.set_text("Turns = " + str(0))
    
# The game logic is implemented here:
# Flip current card, save it as the first card, next state is 1.
# Flip current card, save it as the second card, next state is 2.
# Check if the 1st & 2nd cards match,
#  - if not flip them
#  - regardless of what happened in that check, flip current 
#    card, save it as the first card, next state is 1.

def mouseclick(pos):
    global state, exp_cards, turns
    
    current_idx = pos[0] // 50 # index of the card clicked
    # memory states  
    if current_idx not in exp_cards:
        if state == 0:
            state = 1
            exp_cards = [current_idx]
        elif state == 1:
            state = 2
            exp_cards.append(current_idx)
        else:
            state = 1
            turns += 1
            label.set_text("Turns = " + str(turns))
            if deck[exp_cards[-1]] != deck[exp_cards[-2]]:
                exp_cards.pop()
                exp_cards.pop()
            exp_cards.append(current_idx)  
        print "List of exposed cards:", exp_cards
                        
# cards are logically 50x100 pixels in size  
#
#
def draw(canvas):
    global frameX, frameY, exposed, exp_cards
    
    # draws the shuffled deck on the canvas
    #if 
    for i in range(len(deck)):
        deck_pos = 16 + 50 * i
        canvas.draw_text(str(deck[i]), (deck_pos, 66), 40, 'Red')
        canvas.draw_line((i*50, 0), (i*50, 100), 2, 'Black')
        if i not in exp_cards:
            deck_pos2 = 50 * (i + 1)
            canvas.draw_line((deck_pos2-50, 100), (deck_pos2, 100), 200, 'Green')
 

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", frameX, frameY)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
print label.get_text()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
