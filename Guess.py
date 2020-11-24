# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# helper function to start and restart the game
def new_game(g=0):
    # initializing global variables used    
    global secret_number
    global f
    f = g
    global n
    if f == 0:
        secret_number = random.randrange(0, 100)
        n = math.ceil(math.log(101, 2))
        print "range[0,100)"
    else:
        secret_number = random.randrange(0, 1000)
        n = math.ceil(math.log(1001, 2))
        print "range[0,1000)"
    global c
    c = 0
    
    print "remain:", n
    #print "s:", secret_number
    
# defining event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game  
    print '\n'
    new_game()
    
    #print "remain:", n
    #print "s:", secret_number

def range1000():
    # button that changes the range to [0,1000) and starts a new game      
    print '\n'
    new_game(1)

    #print "s:", secret_number
    
def input_guess(guess):
    # main game logic goes here	
    global n
    global c
    if c < n:
        global secret_number
        c = c + 1

        n_guess = int(guess)
        print "Guess was", n_guess
        if secret_number < n_guess:
            print "Lower"
            print "remain:", n-c 
            print '\n'
        if secret_number > n_guess:
            print "Higher"
            print "remain:", n-c
            print '\n'
        if secret_number == n_guess:
            print "Correct"
            print "remain:", n-c 
            print "You win! start new game!"
            print '\n'
            new_game(f)
            
        if c == n:
            print "You run out ot times! start new game! correct is", secret_number
            print '\n'
            new_game(f)
        
# creating frame
frame = simplegui.create_frame('Guess the number!', 200, 200)

# registering event handlers for control elements and start frame
inp = frame.add_input('My Guess', input_guess, 100)
range100 = frame.add_button('range100', range100, 100)
range1000 = frame.add_button('range1000', range1000, 100)

# calling new_game 
new_game()
