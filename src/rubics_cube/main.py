from pprint import pprint

from .state import RCState


class NDRubicsCube:
    def __init__(self, n):
        self.n = n
        self.state = RCState(n)
        self.moves = None


if __name__ == "__main__":
    n = 20
    print(f"Creating {n}D Rubics Cube\n\n")
    cube = NDRubicsCube(n)

    print("State permutations:")
    pprint(cube.state._permutations.__dict__)
    print("\nState orientations:")
    pprint(cube.state._orientations.__dict__)
