#!/usr/bin/env python3
from cars import Car
from random import randint
BASE_SPEED = 10
BASE_INTERVAL_MIN = 500
BASE_INTERVAL_MAX = 1000

def get_spawn_delay():
    # Calculate how much faster we are going compared to the start
    speed_ratio = Car.car_speed / BASE_SPEED

    # Divide the intervals by that ratio
    current_min = int(BASE_INTERVAL_MIN / speed_ratio)
    current_max = int(BASE_INTERVAL_MAX / speed_ratio)

    return randint(current_min, current_max)
