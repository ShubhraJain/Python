# To use the stop watch, please visit http://www.codeskulptor.org/#user30_XUWrp4Pw1wMWtFC_0.py
# The game involved is, it draws the number of successful stops at a whole second versus the total number of stops and the 
# score is shown on the top right corner of the canvas

#import modules
import simplegui

# define global variables
interval = 0
time = "0:00.0"
success = 0
attempts = 0
    
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if (t < 10):
        return "0:00." + str(t)
    elif (t >= 10 and t < 100):
        sec = t // 10
        tenth_sec = t % 10
        return "0:0" + str(sec) + "." + str(tenth_sec)
    elif (t >= 100 and t < 600):
        sec = t // 10
        tenth_sec = t % 10
        return "0:" + str(sec) + "." + str(tenth_sec)
    else:
        mins = t // 600
        t = t - mins * 600
        secs = t % 600
        if secs < 100:
            return str(mins) + ":0" + str(secs/10) + "." + str(secs % 10)
        else:
            return str(mins) + ":" + str(secs/10) + "." + str(secs % 10)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global interval
    global success
    global attempts
    timer.stop()
    attempts = attempts + 1
    if (interval % 10 == 0):
        success += 1

# stops the timer (if running) and resets the timer to 0 and 
# clears the success/attempts numbers.
def reset():
    global interval
    global attempts
    global success
    timer.stop()
    interval = 0
    attempts = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def increase_time():
    global interval
    interval += 1
    return interval

# define draw handler
def draw(canvas):
    global success
    global attempts
    canvas.draw_text(format(interval), [100, 100], 30, "Aqua")    
    s = "%d/%d" %(success, attempts)
    canvas.draw_text(s, [220, 20], 20, "Red")

# create frame
    frame = simplegui.create_frame("Stop Watch", 275, 200)

# register event handlers
    frame.set_draw_handler(draw)

    frame.add_button("Start", start, 100)
    frame.add_button("Stop", stop, 100)
    frame.add_button("Reset", reset, 100)

    timer = simplegui.create_timer(100, increase_time)

# start frame
    frame.start()
