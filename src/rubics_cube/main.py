from __future__ import annotations
from numpy import array, zeros, roll, ndarray, sum as np_sum
from math import factorial

from .move import _Move, Moves

class RK:
    def __init__(self):
        self._cp = array([0,1,2,3,4,5,6,7])
        self._co = array([0,0,0,0,0,0,0,0])
        self._ep = array([0,1,2,3,4,5,6,7,8,9,10,11])
        self._eo = array([0,0,0,0,0,0,0,0,0,0,0,0])
    
    def apply_move(self, move: _Move):
        self._cp = self._cp[move.P_cp]
        self._co = (self._co[move.P_cp] + move.delta_co) % 3
        self._ep = self._ep[move.P_ep]
        self._eo = (self._eo[move.P_ep] + move.delta_eo) % 2
    
    def _permutation_to_index(self, permutation):
        index = 0
        for i in range(1, len(permutation)):
            index += np_sum(permutation[:i]>permutation[i]) * factorial(i)
        return index

    def _orientation_to_index(self, orientation, base):
        value = 0
        for d in orientation:
            value = value * base + d
        return value
    
    def __str__(self):
        return (
            f"corner permutation {self._cp} -> {self._permutation_to_index(self._cp)}\n"
            f"corner orientation {self._co} -> {self._orientation_to_index(self._co, 3)}\n"
            f"edge permutation {self._ep} -> {self._permutation_to_index(self._ep)}\n"
            f"enge orientation {self._eo} -> {self._orientation_to_index(self._eo, 2)}\n"
        )
    
    def __eq__(self, other: RK):              # type: ignore
        return (
            (self._cp == other._cp).all() and
            (self._co == other._co).all() and
            (self._ep == other._ep).all() and
            (self._eo == other._eo).all()
        )