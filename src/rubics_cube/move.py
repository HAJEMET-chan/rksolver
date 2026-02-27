from numpy import (
    array,
    zeros, 
    ndarray, 
    issubdtype, 
    integer, 
    unique,
    any as np_any,
)

class _Move:
    def __init__(
        self,
        P_cp: ndarray = zeros(4),
        delta_co: ndarray = zeros(4),
        P_ep: ndarray = zeros(4),
        delta_eo: ndarray = zeros(4),
    ):
        self.P_cp = P_cp
        self.delta_co = delta_co
        self.P_ep = P_ep
        self.delta_eo = delta_eo

        if not self._validate_move():
            raise ValueError("Invalid _Move: violates cube rules")
    
    def _validate_move(self) -> bool:
        # types checking
        for arr in [self.P_cp, self.delta_co, self.P_ep, self.delta_eo]:
            if not isinstance(arr, ndarray) or not issubdtype(arr.dtype, integer):
                return False
        # shape checking
        for arr in [self.P_cp, self.delta_co, self.P_ep, self.delta_eo]:
            if arr.shape != (4,):
                return False
        
        # P_cp checking
        if min(self.P_cp) < 0 or max(self.P_cp) > 7:
            return False
        if len(unique(self.P_cp)) != 4:
            return False
        
        # P_ep checking
        if min(self.P_ep) < 0 or max(self.P_ep) > 11:
            return False
        if len(unique(self.P_ep)) != 4:
            return False
        
        # delta_co checking
        if sum(self.delta_co) % 3 != 0:
            return False
        if np_any(self.delta_co < 0) or np_any(self.delta_co > 2):
            return False
        
        # delta_eo checking
        if sum(self.delta_eo) % 2 != 0:
            return False
        if np_any(self.delta_eo < 0) or np_any(self.delta_eo > 1):
            return False
        
        return True
    
class Moves:
    U = _Move(
        P_cp=array([3, 0, 1, 2]),
        delta_co=zeros(4, dtype=int),
        P_ep=array([0, 1, 2, 3]),
        delta_eo=zeros(4, dtype=int)
    )
    D = _Move(
        P_cp=array([4, 5, 6, 7]),
        delta_co=zeros(4, dtype=int),
        P_ep=array([8, 9, 10, 11]),
        delta_eo=zeros(4, dtype=int)
    )
    L = _Move(
        P_cp=array([0, 7, 4, 3]),
        delta_co=array([1, 2, 1, 2]),
        P_ep=array([3, 10, 7, 11]),
        delta_eo=zeros(4, dtype=int)
    )
    R = _Move(
        P_cp=array([1, 2, 5, 6]),
        delta_co=array([1, 2, 1, 2]),
        P_ep=array([1, 5, 9, 6]),
        delta_eo=zeros(4, dtype=int)
    )
    F = _Move(
        P_cp=array([0, 1, 6, 7]),
        delta_co=array([1, 2, 1, 2]),
        P_ep=array([0, 4, 8, 7]),
        delta_eo=array([1, 1, 1, 1])
    )
    B = _Move(
        P_cp=array([2, 3, 4, 5]),
        delta_co=array([1, 2, 1, 2]),
        P_ep=array([2, 11, 10, 5]),
        delta_eo=array([1, 1, 1, 1])
    )

    @classmethod
    def all(cls):
        return [cls.U, cls.D, cls.L, cls.R, cls.F, cls.B]