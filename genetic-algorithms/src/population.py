# Population Class | Genetic Algorithm

from random import randint
from random import choice


class Population:
    class Member:
        def __init__(self):
            self.directions = ["U", "D", "L", "R"]
            self.DNA = []   # TODO
            self.fitness = 0

        def get_fitness(self, feedback):
            pass

        def mutate(self, mutation_rate):
            pass

    def __init__(self, spawn, pop_size=10, mutation_rate=0.1):
        self.spawn = spawn  # (x, y) tuple, np format
        self.members = []   # TODO

    def batch_fitness(self):
        pass

    def batch_mutate(self):
        pass

    def crossover(self):
        pass

    def selection(self):
        pass
