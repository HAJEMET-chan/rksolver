from itertools import product, combinations
from typing import Dict, List, Tuple
from pprint import pprint

Coord = Tuple[int, ...]


def generate_hypercube_coords_no_middle(
    n: int,
) -> Dict[int, List[Coord]]:
    coords_by_zeros: Dict[int, List[Coord]] = {
        k: [] for k in range(n - 1)
    }  # zeros <= n-2

    for coord in product([-1, 0, 1], repeat=n):
        if coord == (0,) * n:
            continue
        zeros = coord.count(0)
        if zeros >= n - 1:
            continue
        coords_by_zeros[zeros].append(coord)

    return coords_by_zeros
