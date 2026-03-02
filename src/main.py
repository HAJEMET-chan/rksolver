from numpy import array

from .rubics_cube.main import RK
from .rubics_cube.move import Moves, _Move


def main():

    cube = RK()

    print(cube)

    while True:

        notation_input = input("Enter move notation (or 'exit' to quit): ").upper()

        if notation_input == "exit":
            break

        notations = notation_input.split()

        moves: list[_Move] = []                               # type: ignore

        for notation in notations:
            tmp_move = Moves.get_move_by_notation(notation)

            if tmp_move is None:
                print(f"Invalid notation {notation}")
                continue

            moves.append(tmp_move)
        

        for move in moves:
            cube.apply_move(move)

        print(cube)

def test_move():

    cube = RK()

    print(cube)

    move = Moves.F

    for _ in range(4):
        cube.apply_move(move)
        print(cube)


    



    
