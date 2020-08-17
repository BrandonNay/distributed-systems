from mpi4py import MPI
import numpy as np
import platform
import os

from .population import Population


class Node:
    class State:
        def __init__(self, name):
            self.name = name

    def __init__(self):
        self.comm = MPI.COMM_WORLD
        self.rank = self.comm.Get_rank()
        self.yeet = self.comm.size % (self.rank + 1)

        if self.rank == 0:
            self.build_environment()
        if self.rank == 1:
            self.spawn_population("*", (20, 5))
        if self.rank == 2:
            self.spawn_population("~", (20, 39))
        if self.rank == 3:
            self.spawn_population("+", (20, 74))

    def build_environment(self):
        """Rank-0, constructs playing field. PuTTY req 24row x 80 col"""

        self.field = np.full((23, 80), " ")

        for x in range(18):
            self.field[6][x+30] = "#"
        self.field[5][28] = "#"
        self.field[5][29] = "#"
        self.field[5][48] = "#"
        self.field[5][49] = "#"
        self.field[2][39] = "@"

    def print_environment(self):
        """Rank-0, displays current playing field state"""

        out_string = ""
        for i in range(23):
            for j in range(80):
                out_string += self.field[i, j]
        os.system(r"printf '\033[2J'")      # clear terminal
        os.system(f"echo '{out_string}'")   # print

    def report(self):
        print(f"HOST:{platform.node()} | R:{self.rank}")

    def send_receive(self):
        self.state = self.State(f"we da {self.rank} muzikj")
        self.states = self.comm.gather(self.state, root=0)

        print(self.states)

    def spawn_population(self, indentifier, start_position):
        self.indentifier = indentifier
        self.pop = Population(start_position)


if __name__ == "__main__":
    burger = Node()
    burger.report()
    burger.send_receive()
