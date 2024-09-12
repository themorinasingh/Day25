from turtle import Turtle
import time

class my_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 0

    def move_and_write(self, position, state_name):
        self.goto(position)
        self.write(arg=state_name, align="center", move=False, font=("Ariel", 16, "normal"))




