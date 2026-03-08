from enum import Enum

from ..rubics_cube.main import RС
from ..rubics_cube.move import _Move
from ..rubics_cube.utils import permutation_to_index, orientation_to_index

def collect_move_data(cube: RС, prev_cube: RС, move: _Move):
    data = {
            "move": move.notation,
            "cp": cube._cp.copy(),
            "co": cube._co.copy(),
            "ep": cube._ep.copy(),
            "eo": cube._eo.copy(),
            "index_cp": permutation_to_index(cube._cp),
            "index_co": orientation_to_index(cube._co, 3),
            "index_ep": permutation_to_index(cube._ep),
            "index_eo": orientation_to_index(cube._eo, 2),
            "P_cp": move.P_cp,
            "delta_co": move.delta_co,
            "P_ep": move.P_ep,
            "delta_eo": move.delta_eo,
            "index_P_cp": permutation_to_index(move.P_cp),
            "index_delta_co": orientation_to_index(move.delta_co, 3),
            "index_P_ep": permutation_to_index(move.P_ep),
            "index_delta_eo": orientation_to_index(move.delta_eo, 2),
            "prev_cp": prev_cube._cp.copy(),
            "prev_co": prev_cube._co.copy(),
            "prev_ep": prev_cube._ep.copy(),
            "prev_eo": prev_cube._eo.copy(),
            "index_prev_cp": permutation_to_index(prev_cube._cp),
            "index_prev_co": orientation_to_index(prev_cube._co, 3),
            "index_prev_ep": permutation_to_index(prev_cube._ep),
            "index_prev_eo": orientation_to_index(prev_cube._eo, 2),
            "delta_index_cp": permutation_to_index(cube._cp) - permutation_to_index(prev_cube._cp),
            "delta_index_co": orientation_to_index(cube._co, 3) - orientation_to_index(prev_cube._co, 3),
            "delta_index_ep": permutation_to_index(cube._ep) - permutation_to_index(prev_cube._ep),
            "delta_index_eo": orientation_to_index(cube._eo, 2) - orientation_to_index(prev_cube._eo, 2),
        }
    return data

class Move_data_columns(Enum):
    MOVE = "move"
    CP = "cp"
    CO = "co"
    EP = "ep"
    EO = "eo"
    INDEX_CP = "index_cp"
    INDEX_CO = "index_co"
    INDEX_EP = "index_ep"
    INDEX_EO = "index_eo"
    P_CP = "P_cp"
    DELTA_CO = "delta_co"
    P_EP = "P_ep"
    DELTA_EO = "delta_eo"
    INDEX_P_CP = "index_P_cp"
    INDEX_DELTA_CO = "index_delta_co"
    INDEX_P_EP = "index_P_ep"
    INDEX_DELTA_EO = "index_delta_eo"
    PREV_CP = "prev_cp"
    PREV_CO = "prev_co"
    PREV_EP = "prev_ep"
    PREV_EO = "prev_eo"
    INDEX_PREV_CP = "index_prev_cp"
    INDEX_PREV_CO = "index_prev_co"
    INDEX_PREV_EP = "index_prev_ep"
    INDEX_PREV_EO = "index_prev_eo"
    DELTA_INDEX_CP = "delta_index_cp"
    DELTA_INDEX_CO = "delta_index_co"
    DELTA_INDEX_EP = "delta_index_ep"
    DELTA_INDEX_EO = "delta_index_eo"