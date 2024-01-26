import turtle
from random import randint
import random

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Catch The Turtle")
FONT = ('Arial', 30, 'normal')
score = 0
game_over = False

turtle_list = []

#SCORE TURTLE
score_turtle = turtle.Turtle(visible=False)

#COUNTDOWN TURTLE
countdown_turtle = turtle.Turtle(visible=False)


def setup_score_turtle():
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle(visible=False)

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        t.hideturtle()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x, y)
    turtle_list.append(t)

coordinates_dict = {}

def setup_turtles():
    for a in range(0,10):
        
        x = randint(-400, 400)
        y = randint(-350, 350)
        if len(coordinates_dict) > 0 and x in coordinates_dict[a-1]:
            x = x*2/3
        if len(coordinates_dict) > 0 and y in coordinates_dict[a-1]:
            y = y*2/3

        coordinates_dict[a] = (x,y)
        a += 1
        print(coordinates_dict)

    i = 0    
    for i in range(0,10):
        i+=1
        for x,y in coordinates_dict.values():
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_random():
    screen.update()
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_random, 500)

def countdown(time):
    global game_over
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0, y - 35)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)
        screen.update()



turtle.tracer(0)
screen.update()
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_random()
countdown(10)
turtle.tracer(1) 
screen.update()

turtle.mainloop()