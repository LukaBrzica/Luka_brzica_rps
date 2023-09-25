# This file was created by Luka Brzica on 9/6/2023

'''
This will be the start of my rock, paper, scissors game. I'll start by coding the randomizing function of options.

Goals:
When a user click on their choice, the computer randomly chooses and displays the result

'''


# import package
import turtle
from turtle import *
from random import randint

# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
 
# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

# setup the screen using the turtle module
screen = turtle.Screen()

screen.setup(WIDTH + 4, HEIGHT + 8)  # factors due to window borders & title bar

screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

# canvas object
cv = screen.getcanvas()

# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')

# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()

# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')

# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()

# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')

# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)

    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)

    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()

    # set the position of the rock_instance
    rock_instance.setpos(x,y)

 

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)

    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)

    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()

    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)

    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)

    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()

    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)

# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup()

# place position of objects
show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)


# this function uses and x y value, an obj, and width and height
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick

def mouse_pos(x, y):
    if collide(x,y,rock_instance, rock_w, rock_h):
        text.clear()
        text.write("you chose rock!!!", False, "left", ("Arial", 24, "normal"))

        # I need the computer to randomly choose an option...
        # I also need to display what the computer chose and communicate winner to user
        def computer_choice():
            choice = randint(0,2)
            if choice == 0:
                show_rock(-300,0)
                text.clear()
                paper_instance.hideturtle()
                scissors_instance.hideturtle()
                text.write("cpu chose rock!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("it is a tie", False, "right", ("Arial", 24, "normal"))

            elif choice == 1:
                show_paper(0,0)
                text.clear()
                scissors_instance.hideturtle()
                text.write("cpu chose paper!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("you lose", False, "right", ("Arial", 24, "normal"))

            elif choice == 2:
                show_scissors(300,0)
                text.clear()
                paper_instance.hideturtle()
                text.write("cpu chose scissors!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("you win", False, "right", ("Arial", 24, "normal"))

        computer_choice()
    elif collide(x,y,paper_instance, paper_w, paper_h):
        text.clear()
        text.write("you chose paper!!!", False, "left", ("Arial", 24, "normal"))
        def computer_choice():
            choice = randint(0,2)
            if choice == 0:
                show_rock(-300,0)
                text.clear()
                scissors_instance.hideturtle()
                text.write("cpu chose rock!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("you win", False, "right", ("Arial", 24, "normal"))

            elif choice == 1:
                show_paper(0,0)
                text.clear()
                rock_instance.hideturtle()
                scissors_instance.hideturtle()
                text.write("cpu chose paper!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("it is a tie", False, "right", ("Arial", 24, "normal"))

            elif choice == 2:
                show_scissors(300,0)
                text.clear()
                rock_instance.hideturtle()
                text.write("cpu chose scissors!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("you lose", False, "right", ("Arial", 24, "normal"))

        computer_choice()
    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        text.clear()
        text.write("you chose scissors!!!", False, "left", ("Arial", 24, "normal"))

        # determine computers random choice and hide unused choices
        def computer_choice():
            choice = randint(0,2)
            if choice == 0:
                show_rock(-300,0)
                text.clear()
                paper_instance.hideturtle()
                text.write("cpu chose rock!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("you lose", False, "right", ("Arial", 24, "normal"))

            elif choice == 1:
                show_paper(0,0)
                text.clear()
                rock_instance.hideturtle()
                text.write("cpu chose paper!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("you win", False, "right", ("Arial", 24, "normal"))

            elif choice == 2:
                show_scissors(300,0)
                text.clear()
                rock_instance.hideturtle()
                paper_instance.hideturtle()
                text.write("cpu chose scissors!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                text.write("it is a tie", False, "right", ("Arial", 24, "normal"))

        computer_choice()
    else:
        print("you chose nothing!!")

text.setpos(0,150)
text.write("Choose rock or paper or scissors", False, "left", ("Arial", 24, "normal"))

# use this to get mouse position
screen.onclick(mouse_pos)

# runs mainloop for Turtle so you are able to run it multiple times - required to be last
screen.mainloop()