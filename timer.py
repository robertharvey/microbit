# 60 second timer for playing games like Articulate

from microbit import *

MAX_TIME = 60

ONE_SECOND = 1000
FINAL_DISPLAY_TIME = 5*3*400

STATE_STOPPED = 0
STATE_RUNNING = 1
STATE_UPDATE = 2
STATE_FINISHED = 3

state = STATE_STOPPED
old_state = STATE_STOPPED

start_time = 0
do_display = False
clock = 0

finished = [Image("00000:"
                  "00000:"
                  "00900:"
                  "00000:"
                  "00000:"), 
            Image("00000:"
                  "09990:"
                  "09090:"
                  "09990:"
                  "00000:"),
            Image("99999:"
                  "90009:"
                  "90009:"
                  "90009:"
                  "99999:")
            ]

def show_dot(pos, b):
    dots = [ [2,0], [3,0], [4,0], [4,1], [4,2], [4,3], [4,4], [3,4], [2,4], [1,4], [0,4], [0,3], [0,2], [0,1], [0,0], [1,0] ]
    pos = pos % len(dots)
    display.set_pixel(dots[pos][0], dots[pos][1], b)

def show_dots(pos):
    display.clear()
    for p in range(0, 5):
        if (pos - p) < 0:
            break
        show_dot(pos - p, 9-p)


# Point to start button first time in
display.show([Image.ARROW_W,' '], loop=True, wait=False)

while True:

    # Start timer
    if button_a.was_pressed():
        state = STATE_UPDATE
        start_time = last_time = running_time()
        clock = 0
    
    # Reset
    if button_b.was_pressed():
        state = STATE_STOPPED
        start_time = 0
        display.clear()

    # Update every second when running
    if state == STATE_RUNNING and running_time() > last_time + ONE_SECOND:
        last_time = running_time()
        state = STATE_UPDATE
    
    elif state == STATE_FINISHED and running_time() > last_time + FINAL_DISPLAY_TIME:
        last_time = running_time()
        display.clear()
        state = STATE_STOPPED
        
    if state == STATE_UPDATE:
        time = int(MAX_TIME-(last_time-start_time)/1000)
        if time <= 0:
            state = STATE_FINISHED
            display.show(finished, delay=400, wait=False, loop=True)
        else:
            state = STATE_RUNNING
            if time > 10 and time % 10 == 0:
                display.show(time)
            elif time > 9:
                show_dots(clock)
                clock = clock + 1
            else:
                display.show(str(time), wait=False)
        
    sleep(50)