from numpy import array, zeros, roll

from .move import _Move


class RK:
    def __init__(self):
        self._cp = array(range(8))
        self._co = zeros(8)
        self._ep = array(range(12))
        self._eo = zeros(12)
    
    def apply_move(self, move: _Move):
        # ===== Corners =====
        cp_tmp = self._cp.copy()
        co_tmp = self._co.copy()

        idx = move.P_cp

        # 4-cycle permutation
        self._cp[idx] = cp_tmp[roll(idx, -1)]

        # orientation update
        self._co[idx] = (
            co_tmp[roll(idx, -1)] + move.delta_co
        ) % 3


        # ===== Edges =====
        ep_tmp = self._ep.copy()
        eo_tmp = self._eo.copy()

        idx = move.P_ep

        # 4-cycle permutation
        self._ep[idx] = ep_tmp[roll(idx, -1)]

        # orientation update
        self._eo[idx] = (
            eo_tmp[roll(idx, -1)] + move.delta_eo
        ) % 2