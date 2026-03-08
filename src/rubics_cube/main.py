from __future__ import annotations
from numpy import array, copy

from .move import _Move
from .utils import orientation_to_index, permutation_to_index

class RС:
    def __init__(self):
        self._cp = array([0,1,2,3,4,5,6,7])
        self._co = array([0,0,0,0,0,0,0,0])
        self._ep = array([0,1,2,3,4,5,6,7,8,9,10,11])
        self._eo = array([0,0,0,0,0,0,0,0,0,0,0,0])
    
    def apply_move(self, move: _Move, times: int = 1, copy: bool = False):

        if copy:
            cube = self.copy()
        else:
            cube = self
        
        for _ in range(times):
            cube._cp = cube._cp[move.P_cp]
            cube._co = (cube._co[move.P_cp] + move.delta_co) % 3
            cube._ep = cube._ep[move.P_ep]
            cube._eo = (cube._eo[move.P_ep] + move.delta_eo) % 2
        
        return cube

    def reset(self):
        self._cp = array([0,1,2,3,4,5,6,7])
        self._co = array([0,0,0,0,0,0,0,0])
        self._ep = array([0,1,2,3,4,5,6,7,8,9,10,11])
        self._eo = array([0,0,0,0,0,0,0,0,0,0,0,0])

    def copy(self):
        new_cube = RС()
        new_cube._cp = self._cp.copy()
        new_cube._co = self._co.copy()
        new_cube._ep = self._ep.copy()
        new_cube._eo = self._eo.copy()
        return new_cube
    
    def __eq__(self, other: RС):              # type: ignore
        return (
            (self._cp == other._cp).all() and
            (self._co == other._co).all() and
            (self._ep == other._ep).all() and
            (self._eo == other._eo).all()
        )

    def print_cubie(self):
        print("corner permutation: ", self._cp)
        print("corner orientation: ", self._co)
        print("edge permutation: ", self._ep)
        print("edge orientation: ", self._eo)

    def print_coordinates(self):
        print("corner permutation index: ", permutation_to_index(self._cp))
        print("corner orientation index: ", orientation_to_index(self._co, 3))
        print("edge permutation index: ", permutation_to_index(self._ep))
        print("edge orientation index: ", orientation_to_index(self._eo, 2))

    def print_state(self):
        self.print_cubie()
        self.print_coordinates()

    @property
    def cubie_state(self):
        return self._cp, self._co, self._ep, self._eo
    
    @property
    def coordinate_state(self):
        return (
            permutation_to_index(self._cp),
            orientation_to_index(self._co, 3),
            permutation_to_index(self._ep),
            orientation_to_index(self._eo, 2)
        )