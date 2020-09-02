# Population Class | Genetic Algorithm

from random import randint
from random import choice


class Population:
    class Member:
        def __init__(self, lifespan=50, write_dna=True):
            self.lifespan = lifespan
            self.fitness = 0
            self.directions = ["U", "D", "L", "R"]
            if write_dna:
                self.DNA = [choice(self.directions) for x in range(self.lifespan)]
            else:
                self.DNA = []

        def __eq__(self, other):
            return self.fitness == other

        def __ne__(self, other):
            return self.fitness != other

        def __lt__(self, other):
            return self.fitness < other

        def __gt__(self, other):
            return self.fitness > other

        def get_fitness(self, feedback):
            pass

        def mutate(self, mutation_rate):
            for i in range(len(self.DNA)):
                chance = randint(0, 100)/100
                if chance < mutation_rate:
                    self.DNA[i] = choice(self.directions)

    def __init__(self, spawn, pop_size=10, mutation_rate=0.1):
        self.spawn = spawn  # (x, y) tuple, np format
        self.population_size = pop_size
        self.mutation_rate = mutation_rate
        self.members = [self.Member() for x in range(self.population_size)]

    def batch_fitness(self):
        for x in self.members:
            x.get_fitness() # TODO

    def batch_mutate(self):
        for x in self.members:
            x.mutate(self.mutation_rate)

    def crossover(self):
        new_pop = []
        parents = self.selection()

        for x in range(self.population_size//2):
            p1 = choice(parents)
            p2 = choice(parents)

            child1 = self.Member(lifespan=p1.lifespan, write_dna=False)
            child2 = self.Member(lifespan=p1.lifespan, write_dna=False)

            pos = randint(0, p1.lifespan)   # crossover point
            child1.DNA = p1.DNA[:pos] + p2.DNA[pos:]
            child2.DNA = p2.DNA[:pos] + p1.DNA[pos:]

            new_pop.append(child1)
            new_pop.append(child2)

        self.members = new_pop

    def selection(self):
        self.members.sort(reverse=True)
        return self.members[0:self.population_size//2]
