# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction:
        ball_pos=[300,200]
        ball_vel=[1,random.random() * 2 + -1]
    else :
        ball_pos=[300,200]
        ball_vel=[-1,random.random() * 2 + -1]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=160
    paddle2_pos=160
    paddle1_vel=0
    paddle2_vel=0
    score1=0
    score2=0
    spawn_ball(RIGHT)
    
        

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
 
        
   
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[0]<=30.5 :
        if paddle1_pos<=ball_pos[1]+BALL_RADIUS and ball_pos[1]-BALL_RADIUS<=paddle1_pos+80:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]=ball_vel[0]+.5
            ball_vel[1]=random.random() * 5 + -1
       
        else:
            spawn_ball(RIGHT)
            score1=score1+1
    elif ball_pos[0]>=569.5:
            if paddle1_pos<=ball_pos[1]+BALL_RADIUS and ball_pos[1]-BALL_RADIUS<=paddle1_pos+80:
                ball_vel[0]=-ball_vel[0]
                ball_vel[0]=ball_vel[0]-.5
                ball_vel[1]=random.random() * 5 + -1
                
            else:
                spawn_ball(LEFT)
                score2=score2+1
    if ball_pos[1]<=20 or ball_pos[1]>=380:
        ball_vel[1]=-ball_vel[1]
    ball_pos[0]=ball_pos[0]+ball_vel[0]
    ball_pos[1]=ball_pos[1]+ball_vel[1]
            
    # draw ball
    c.draw_circle(ball_pos,20,2,'Red','white')
    
    # update paddle's vertical position, keep paddle on the screen
    
    if(paddle1_pos>0 and paddle1_pos<320):
        paddle1_pos=paddle1_pos+paddle1_vel
        paddle2_pos=paddle2_pos+paddle2_vel
    # draw paddles
    c.draw_polyline([[4,paddle1_pos],[4,paddle1_pos+PAD_HEIGHT ]],PAD_WIDTH,'white')
    c.draw_polyline([[WIDTH - 4,paddle2_pos],[WIDTH - 4,paddle2_pos+PAD_HEIGHT ]],PAD_WIDTH,'white')
    # draw scores
    c.draw_text(str(score2),(100,50),20,'white')
    c.draw_text(str(score1),(400,50),20,'white')
        
def keydown(key):
    global paddle1_vel, paddle2_vel,paddle1_pos,paddle2_pos

    if key==simplegui.KEY_MAP["left"]:
        paddle1_vel=-3
        paddle2_vel=-3
        paddle1_pos=paddle1_pos+paddle1_vel
        paddle2_pos=paddle2_pos+paddle2_vel
    elif key==simplegui.KEY_MAP["right"]:
        paddle1_vel=3
        paddle2_vel=3
        paddle1_pos=paddle1_pos+paddle1_vel
        paddle2_pos=paddle2_pos+paddle2_vel
    elif key==simplegui.KEY_MAP["down"]:
        paddle1_vel=3
        paddle2_vel=3
        paddle1_pos=paddle1_pos+paddle1_vel
        paddle2_pos=paddle2_pos+paddle2_vel
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel=-3
        paddle2_vel=-3
        paddle1_pos=paddle1_pos+paddle1_vel
        paddle2_pos=paddle2_pos+paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key==simplegui.KEY_MAP["left"]:
        paddle1_vel=0
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["right"]:
        paddle1_vel=0
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["down"]:
        paddle1_vel=0
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel=0
        paddle2_vel=0
   


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
