#!/usr/bin/env python3
from turtle import Screen, done
from cars import Car
from pedestrian import Pedestrian
from level import Level
from spawn_rate import get_spawn_delay
from random import randint
import time
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.colormode(255)
screen.listen()
game_is_on = True
cars = []
def make_cars():
    if game_is_on:
        no_of_cars = randint(0, 7)
        for _ in range(no_of_cars):
            car = Car()
            cars.append(car)
        screen.ontimer(make_cars, get_spawn_delay())
def move_cars():
    for each_car in cars:
        each_car.move()
def check_collisions():
    for each_car in cars:
        if each_car.distance(pedestrian) < 25:
            return False
    return True
def next_level():
    pedestrian.back_home()
    Car.car_speed += 5
    level.increment_score()
make_cars()
pedestrian = Pedestrian()
screen.onkey(pedestrian.move, "Up")
level = Level()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    move_cars()
    game_is_on =  check_collisions()
    if pedestrian.ycor() > 250:
        next_level()
done()
