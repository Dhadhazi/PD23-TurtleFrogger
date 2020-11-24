from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_clearer(self, pos):
        cars_cleared = True
        for car in self.cars:
            if car.distance(300, pos) < 50:
                cars_cleared = False
        return cars_cleared

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            position = random.randint(-250, 250)

            while not self.car_clearer(position):
                position = random.randint(-250, 250)

            new_car = Car(color=random.choice(COLORS), position=position)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT