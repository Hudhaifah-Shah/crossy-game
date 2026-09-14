#!/usr/bin/env python3
from turtle import Turtle
class Pedestrian(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
    def create(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.back_home()
    def move(self):
        self.forward(20)
    def back_home(self):
        self.sety(-277)
