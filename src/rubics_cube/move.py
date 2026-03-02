from numpy import ndarray, array

class _Move:
    def __init__(
        self,
        notation: str,
        P_cp: ndarray,
        delta_co: ndarray,
        P_ep: ndarray,
        delta_eo: ndarray,
    ):
        self.notation = notation
        self.P_cp = P_cp
        self.delta_co = delta_co
        self.P_ep = P_ep
        self.delta_eo = delta_eo


class Moves:

    null_move = _Move(
        notation="null",
        P_cp=array([0,1,2,3,4,5,6,7]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([0,1,2,3,4,5,6,7,8,9,10,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    U = _Move(
        notation="U",
        P_cp=array([3,0,1,2,4,5,6,7]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([1,2,3,0,4,5,6,7,8,9,10,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    U_ = _Move(
        notation="U'",
        P_cp=array([1,2,3,0,4,5,6,7]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([3,0,1,2,4,5,6,7,8,9,10,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    U2 = _Move(
        notation="U2",
        P_cp=array([2,3,0,1,4,5,6,7]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([2,3,0,1,4,5,6,7,8,9,10,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    D = _Move(
        notation="D",
        P_cp=array([0,1,2,3,5,6,7,4]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([0,1,2,3,4,5,6,7,11,8,9,10]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    D_ = _Move(
        notation="D'",
        P_cp=array([0,1,2,3,7,4,5,6]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([0,1,2,3,4,5,6,7,9,10,11,8]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    D2 = _Move(
        notation="D2",
        P_cp=array([0,1,2,3,6,7,4,5]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([0,1,2,3,4,5,6,7,10,11,8,9]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    R = _Move(
        notation="R",
        P_cp=array([4,1,2,0,7,5,6,3]),
        delta_co=array([2,0,0,1,1,0,0,2]),
        P_ep=array([0,4,2,3,9,1,6,7,8,5,10,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    R_ = _Move(
        notation="R'",
        P_cp=array([3,1,2,7,0,5,6,4]),
        delta_co=array([2,0,0,1,1,0,0,2]),
        P_ep=array([0,5,2,3,1,9,6,7,8,4,10,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    R2 = _Move(
        notation="R2",
        P_cp=array([7,1,2,4,3,5,6,0]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([0,9,2,3,5,4,6,7,8,1,10,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    L = _Move(
        notation="L",
        P_cp=array([0,2,6,3,4,1,5,7]),
        delta_co=array([0,1,2,0,1,2,0,0]),
        P_ep=array([0,1,2,6,4,5,11,3,8,9,10,7]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    L_ = _Move(
        notation="L'",
        P_cp=array([0,5,1,3,4,6,2,7]),
        delta_co=array([0,1,2,0,1,2,0,0]),
        P_ep=array([0,1,2,7,4,5,3,11,8,9,10,6]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    L2 = _Move(
        notation="L2",
        P_cp=array([0,6,5,3,4,2,1,7]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([0,1,2,11,4,5,7,6,8,9,10,3]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    F = _Move(
        notation="F",
        P_cp=array([1,5,2,3,0,4,6,7]),
        delta_co=array([1,2,0,0,2,1,0,0]),
        P_ep=array([7,1,2,3,0,5,6,8,4,9,10,11]),
        delta_eo=array([1,0,0,0,1,0,0,1,1,0,0,0]),
    )

    F_ = _Move(
        notation="F'",
        P_cp=array([4,0,2,3,5,1,6,7]),
        delta_co=array([1,2,0,0,2,1,0,0]),
        P_ep=array([4,1,2,3,8,5,6,0,7,9,10,11]),
        delta_eo=array([1,0,0,0,1,0,0,1,1,0,0,0]),
    )

    F2 = _Move(
        notation="F2",
        P_cp=array([5,4,2,3,1,0,6,7]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([8,1,2,3,7,5,6,4,0,9,10,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    B = _Move(
        notation="B",
        P_cp=array([0,1,3,7,4,5,2,6]),
        delta_co=array([0,0,1,2,0,0,2,1]),
        P_ep=array([0,1,5,3,4,10,2,7,8,9,6,11]),
        delta_eo=array([0,0,1,0,0,1,1,0,0,0,1,0]),
    )

    B_ = _Move(
        notation="B'",
        P_cp=array([0,1,6,2,4,5,7,3]),
        delta_co=array([0,0,1,2,0,0,2,1]),
        P_ep=array([0,1,6,3,4,2,10,7,8,9,5,11]),
        delta_eo=array([0,0,1,0,0,1,1,0,0,0,1,0]),
    )

    B2 = _Move(
        notation="B2",
        P_cp=array([0,1,7,6,4,5,3,2]),
        delta_co=array([0,0,0,0,0,0,0,0]),
        P_ep=array([0,1,10,3,4,6,5,7,8,9,2,11]),
        delta_eo=array([0,0,0,0,0,0,0,0,0,0,0,0]),
    )

    @classmethod
    def get_all_moves(cls):
        return [
            cls.U,
            cls.U_,
            cls.U2,
            cls.D,
            cls.D_,
            cls.D2,
            cls.R,
            cls.R_,
            cls.R2,
            cls.L,
            cls.L_,
            cls.L2,
            cls.F,
            cls.F_,
            cls.F2,
            cls.B,
            cls.B_,
            cls.B2,
        ]

    @classmethod
    def get_move_by_notation(cls, notation: str):
        
        all_moves = cls.get_all_moves()

        for move in all_moves:
            if notation == move.notation:
                return move
        
        return None