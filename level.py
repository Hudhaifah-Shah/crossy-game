#!/usr/bin/env python3
from turtle import Turtle
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 255)
        self.show_score()
    def show_score(self):
        self.pendown()
        self.write(f"Level {self.level}", font=("Roboto", 21, "normal"))
    def increment_score(self):
        self.clear()
        self.level += 1
        self.show_score()
