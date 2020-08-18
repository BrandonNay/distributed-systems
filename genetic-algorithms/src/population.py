# Population Class | Genetic Algorithm

from random import randint
from random import choice


class Population:
    class Member:
        def __init__(self):
            self.directions = ["U", "D", "L", "R"]

        def get_fitness(self):
            pass

        def mutate(self):
            pass

    def __init__(self, spawn):
        self.spawn = spawn  # (x, y) tuple, np format

    def batch_fitness(self):
        pass

    def batch_mutate(self):
        pass

    def crossover(self):
        pass

    def selection(self):
        pass
