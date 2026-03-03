from __future__ import annotations
from numpy import array

from .move import _Move
from .utils import orientation_to_index, permutation_to_index

class RС:
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
    
    
    
    def __str__(self):
        return (
            f"corner permutation {self._cp} -> {permutation_to_index(self._cp)}\n"
            f"corner orientation {self._co} -> {orientation_to_index(self._co, 3)}\n"
            f"edge permutation {self._ep} -> {permutation_to_index(self._ep)}\n"
            f"enge orientation {self._eo} -> {orientation_to_index(self._eo, 2)}\n"
        )
    
    def __eq__(self, other: RС):              # type: ignore
        return (
            (self._cp == other._cp).all() and
            (self._co == other._co).all() and
            (self._ep == other._ep).all() and
            (self._eo == other._eo).all()
        )