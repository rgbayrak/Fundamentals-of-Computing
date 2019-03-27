# Implementation of classic arcade game Pong
#
# The objective of this programming assignment is  
# practicing keyboard input/control and lists
#
# Independent Study (Week5)
# Roza Gunes Bayrak
# Vanderbilt University

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 800
HEIGHT = 400       
BALL_RADIUS = 10
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True
paddle1_pos = paddle2_pos = 150
paddle1_vel = paddle2_vel = 0
vel = 2
score1 = 0
score2 = 0
    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    if direction == RIGHT:
        ball_vel = [random.randrange(2, 4), -random.randrange(1,3)]    
    if direction == LEFT:
        ball_vel = [-random.randrange(2, 4), -random.randrange(1,3)]    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)

# /**
#
# 
# 
# param: canvas
# */
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    canvas.draw_text(str(score1), (WIDTH/4 - PAD_WIDTH, 40), 40, "White")
    canvas.draw_text(str(score2), (3*WIDTH/4 - PAD_WIDTH, 40), 40, "White")
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # reflect from the north wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # reflect from the west wall    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH/2:
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + HEIGHT/4: 
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball(LEFT)
            score2 += 1
        
    # reflect from the south wall       
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # reflect from the east wall
    if ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH/2):
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + HEIGHT/4: 
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score1 += 1
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Blue", "White")
    
    # update paddle's vertical position, keep paddle on the screen 
    if paddle1_vel < 0 and paddle1_pos > 0:
        #if paddle1_pos <= HEIGHT - HEIGHT/4 and paddle1_pos > 0:
        paddle1_pos += paddle1_vel
    if paddle2_vel < 0 and paddle2_pos > 0:
        #if paddle1_pos <= HEIGHT - HEIGHT/4 and paddle1_pos > 0:
        paddle2_pos += paddle2_vel
    if paddle1_vel > 0 and paddle1_pos <= HEIGHT - HEIGHT/4: 
        #if paddle2_pos <= HEIGHT - HEIGHT/4 and paddle2_pos > 0:
        paddle1_pos += paddle1_vel
    if paddle2_vel > 0 and paddle2_pos <= HEIGHT - HEIGHT/4: 
        #if paddle2_pos <= HEIGHT - HEIGHT/4 and paddle2_pos > 0:
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_line([0, paddle1_pos],[0, HEIGHT/4 + paddle1_pos], 16, "White")
    canvas.draw_line([WIDTH, paddle2_pos],[WIDTH, HEIGHT/4 + paddle2_pos], 16, "White")   
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):

    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = vel
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = vel

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -vel
 
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0 
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
