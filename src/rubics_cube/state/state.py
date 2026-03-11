from math import factorial
from numpy import array, zeros

from .permutations import Permutations
from .orientations import Orientations


class RCState:
    def __init__(self, n):
        self._permutations = Permutations()
        self._orientations = Orientations()
        self._calculate_state(n)

    def _calculate_state(self, n: int):

        for k in range(n - 1):

            elem_cnt: int = int(
                (factorial(n) / (factorial(n - k) * factorial(k))) * 2 ** (n - k)
            )

            self._permutations.__setattr__(
                f"_{n-k}fp", array(list(range(elem_cnt)), dtype=int)
            )
            self._orientations.__setattr__(f"_{n-k}fo", zeros(elem_cnt, dtype=int))
