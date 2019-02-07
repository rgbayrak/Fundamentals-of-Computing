""" 
"Stopwatch: The Game"
Addition to the stop watch game, this game tests players reflexes. 
Counts how many time they could possibly 
start/stop the game within 0.1 secs?

"""
import simplegui

# define global variables
time = 0
laps = 0 # counts the laps within 0.1 sec
hit = 0 # when clock stopped
state = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    x = time % 10 # 0.1 increments
    y = (time/10) % 60 # seconds
    z = (time/10) / 60 # minutes
    return '%d:%02d.%d' % (z, y, x)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global state
    timer.start()
    state = False
    
def stop():
    global state, hit, laps
    hit += 1
    if (laps % 10) == 0:
        laps += 1
    timer.stop()
    state = True
    
def reset():
    global time, laps, hit, state
    time = 0
    laps = 0 # counts the laps
    hit = 0
    state = False
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    
# define draw handler
def draw_handler(canvas):
    t = format(time)
    canvas.draw_text(str(hit) + "/" + str(laps), (100, 120), 46, 'White')
    canvas.draw_text(str(t), (100, 180), 46, 'White')

    
# create frame
frame = simplegui.create_frame("Stop watch.", 300, 300)

# register event handlers
button1 = frame.add_button("Start", start, 150)
button2 = frame.add_button("Stop", stop, 150)
button3 = frame.add_button("Reset", reset, 150)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

