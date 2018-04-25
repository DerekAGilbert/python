from math import sqrt
from random import randint

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
    def move_rocket(self, x_increment=0, y_increment=1):
        # Increment the y-position of the rocket.
        self.x += x_increment
        self.y += y_increment
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance

class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed


shuttles = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    flights_completed = randint(0, 15)
    shuttles.append(Shuttle(x, y, flights_completed))

rockets = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    rockets.append(Rocket(x, y))

for index, shuttle in enumerate(shuttles):
    print(f'Shuttle {index} has completed {shuttle.flights_completed} flights.')

first_shuttle = shuttles[0]
for index, shuttle in enumerate(shuttles):
    distance = first_shuttle.get_distance(shuttle)
    print(f'The first shuttle is {distance} units away from shuttle {index}.')






# falcon9_1 = Rocket()
# falcon9_2 = Rocket(10, 10)
# distance = falcon9_1.get_distance(falcon9_2)
# for index, falcon_heavy in enumerate(spacex_rockets):
# print(f'falcon9_1 is {distance} units away from falcon9_2')
