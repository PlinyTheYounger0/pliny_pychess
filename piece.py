
from enum import Enum

class Color(Enum):
    WHITE = 'W'
    BLACK = 'B'
class PieceType(Enum):
    KNIGHT = 'N'
    QUEEN = 'Q'
    BISHOP = 'B'
    ROOK = 'R'
    KING = 'K'
    PAWN = 'P'
    
class Piece:
    def __init__(self, row, column, Color, PieceType):
        self.row = row
        self.column = column
        self.color = Color
        self.piece_type = PieceType
        self.rep = Color.value + PieceType.value
        self.valid_moves = []

    def move(row, column):
        pass
    
    def check_valid_moves(row, column):
        pass

class Rook(Piece):
    def __init__(self, row, column, Color, PieceType, has_moved=False):
        super().__init__(row, column, Color, PieceType)

class Knight(Piece):
    def __init__(self, row, column, Color, PieceType):
        super().__init__(row, column, Color, PieceType)

class Bishop(Piece):
    def __init__(self, row, column, Color, PieceType):
        super().__init__(row, column, Color, PieceType)

class Queen(Piece):
    def __init__(self, row, column, Color, PieceType):
        super().__init__(row, column, Color, PieceType)

class King(Piece):
    def __init__(self, row, column, Color, PieceType, has_moved=False):
        super().__init__(row, column, Color, PieceType)

class Pawn(Piece):
    def __init__(self, row, column, Color, PieceType, has_moved=False):
        super().__init__(row, column, Color, PieceType)

