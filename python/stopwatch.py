# template for "Stopwatch: The Game"
import simplegui
# define global variables
mint=0
sec=0
msec=0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
	timer.start()
    
def stop():
	timer.stop()

    
def reset():
	global mint,sec,msec
	mint=0
	sec=0
	msec=0


# define event handler for timer with 0.1 sec interval
def event_handler():
	global mint,sec,msec
	if msec>9:
		msec=0
		sec=sec+1
	elif sec>60:
		min=min+1
		sec=0
	else :
		msec=msec+1




# define draw handler
def draw_handler(canvas):
	canvas.draw_text(str(mint)+":"+str(sec)+"."+str(msec), [100, 100], 12, "Red")


    
# create frame
frame=simplegui.create_frame("Stopwatch",300,300)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("reset",reset,100)
frame.set_draw_handler(draw_handler)



# register event handlers
timer=simplegui.create_timer(100,event_handler)

# start frame

frame.start()
# Please remember to review the grading rubric
