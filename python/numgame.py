import simplegui
import random
import math
mysterynum=0
i=0
def new_game():
	range100()
def range100():
	print 'New game is start'
	print 'guess the nymber between 0 to 100'
	global mysterynum,i
	i=7
	mysterynum=random.randint(0,100)
def range1000():
	print 'New game is start'
	print 'guess the number between 0 to 1000'
	global mysterynum,i
	i=10
	mysterynum=random.randint(0,1000)
def enter_number(guess):
	global mysterynum,i
	print 'guess was'+guess
	print 'remaining chance is'+str(i)
	if i==0:
		print 'you have lost the match'
	elif mysterynum>int(guess):
		print 'Higher'
	elif mysterynum<int(guess):
		print 'Lower'
	else:
		print 'correct'
		
	i=i-1
	
		

frame=simplegui.create_frame("Guess game",300,300)
frame.add_button('range100',range100,100)
frame.add_button('range1000',range1000,100)
frame.add_input('text',enter_number,100)

frame.start()
new_game()
