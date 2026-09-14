#!/usr/bin/env python3
from turtle import Turtle
from random import randint
class Car(Turtle):
    car_speed = 10
    def __init__(self):
        super().__init__()
        self.create_car()
    def create_car(self):
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        r = randint(0,255)
        g = randint(0, 255)
        b = randint(0, 255)
        rgb = (r, g, b)
        self.color(rgb)
        self.setx(300)
        self.sety(randint(-220, 230))
        self.setheading(180)
    def move(self):
        self.forward(self.car_speed)
