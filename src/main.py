from mpi4py import MPI
import platform


class Node:
    class State:
        def __init__(self, name):
            self.name = name

    def __init__(self):
        self.comm = MPI.COMM_WORLD
        self.rank = self.comm.Get_rank()
        self.yeet = self.comm.size % (self.rank + 1)

    def report(self):
        print(f"HOST:{platform.node()} | R:{self.rank}")

    def send_receive(self):
        self.state = self.State(f"we da {self.rank} muzikj")
        self.states = self.comm.gather(self.state, root=0)

        print(self.states)


if __name__ == "__main__":
    burger = Node()
    burger.report()
    burger.send_receive()
