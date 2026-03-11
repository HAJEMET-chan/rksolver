from pprint import pprint

from .state import RCState


class NDRubicsCube:
    def __init__(self, n):
        self.n = n
        self.state = RCState(n)


if __name__ == "__main__":
    n = 6
    print(f"Creating {n}D Rubics Cube\n\n")
    cube = NDRubicsCube(n)
