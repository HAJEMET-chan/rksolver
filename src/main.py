from .rubics_cube.main import RK
from .rubics_cube.move import Moves

moves = {
    "U": Moves.U,
    "D": Moves.D,
    "L": Moves.L,
    "R": Moves.R,
    "F": Moves.F,
    "B": Moves.B,
}

cube = RK()
def main():

    while True:
        print("present state:")
        print(cube._cp)
        print(cube._co)
        print(cube._ep)
        print(cube._eo)
        print("\n"*2)

        print("now we play :")
        inp = input("write your move: ")

        move = moves.get(inp)

        if move is None:
            print("invalid move")
            continue
        
        cube.apply_move(move)
        print("\n"*2)