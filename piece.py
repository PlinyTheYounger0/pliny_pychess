
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
        self.column = column
        self.row = row
        self.color = Color
        self.piece_type = PieceType
        self.rep = Color.value + PieceType.value
        self.valid_moves = []

    def move(self, board, new_row, new_column):
        pass
    
    def check_valid_moves(self, board):
        pass
    

class Rook(Piece):
    def __init__(self, row, column, Color, PieceType, has_moved=False):
        super().__init__(row, column, Color, PieceType)
        self.has_moved = False

        def move(self, board, new_row, new_column):
            self.has_moved = True
            move = (new_row, new_column)
            old_column = self.column
            old_row = self.row

            if move in self.valid_moves:
                board[new_row][new_column] = self
                self.column = new_column
                self.row = new_row
                board[old_row][old_column] = ' *'
            else:
                print('\n***Invalid Move***\n')
                return board, 1

            return board, 0

        def check_valid_moves(self, board):
            self.valid_moves = []

            for column in range(self.column + 1, 9):
                space = board[self.row][column]

                if not isinstance(space, Piece):
                    self.valid_moves.append((self.row, column))
                else:
                    if self.color == space.color:
                        break
                    if self.color != space.color:
                        self.valid_moves.append((self.row, column))
                        break 

            for column in range(self.column - 1, 0, -1):
                space = board[self.row][column]

                if not isinstance(space, Piece):
                    self.valid_moves.append((self.row, column))
                else:
                    if self.color == space.color:
                        break
                    elif self.color != space.color:
                        self.valid_moves.append((self.row, column))
                        break


            for row in range(self.row + 1, 9):
                space = board[row][self.column]
                if not isinstance(space, Piece):
                    self.valid_moves.append((row, self.column))
                else:
                    if self.color == space.color:
                        break
                    if self.color != space.color:
                        self.valid_moves.append((row, self.column))
                        break

            for row in range(self.row - 1, 0, -1):
                space = board[row][self.column]

                if not isinstance(space, Piece):
                    self.valid_moves.append((row, self.column))
                else:
                    if self.color == space.color:
                        break
                    if self.color != space.color:
                        self.valid_moves.append((row, self.column))
                        break


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
    def __init__(self, row, column, Color, PieceType, has_moved=False, in_check=False, mated=False):
        super().__init__(row, column, Color, PieceType)
        self.has_moved = False
        self.in_check = False
        self.mated = False

class Pawn(Piece):
    def __init__(self, row, column, Color, PieceType, has_moved=False):
        super().__init__(row, column, Color, PieceType)
        self.has_moved = False

    def move(self, board, new_row, new_column):
        self.has_moved = True
        move = (new_row, new_column)
        old_column = self.column
        old_row = self.row

        if move in self.valid_moves:
            board[new_row][new_column] = self
            self.column = new_column
            self.row = new_row
            board[old_row][old_column] = ' *'
        else:
            print('\n***Invalid Move***\n')
            return board, 1

        return board, 0

    def check_valid_moves(self, board):
        self.valid_moves = []

        if self.has_moved == False:
            if self.color == Color.WHITE and not isinstance(board[self.row - 1][self.column], Piece) and not isinstance(board[self.row - 2][self.column], Piece):
                self.valid_moves.append((self.row - 2, self.column))
            elif self.color == Color.BLACK and not isinstance(board[self.row + 1][self.column], Piece) and not isinstance(board[self.row + 2][self.column], Piece):
                self.valid_moves.append((self.row + 2, self.column))

        if self.color == Color.WHITE and not isinstance(board[self.row - 1][self.column], Piece):
            if self.row - 1 > 0:
                self.valid_moves.append((self.row - 1, self.column))
        elif self.color == Color.BLACK and not isinstance(board[self.row + 1][self.column], Piece):
            self.valid_moves.append((self.row + 1, self.column))
                    
        if self.column + 1 < 9:
            if self.color == Color.WHITE and isinstance(board[self.row - 1][self.column + 1], Piece):
                piece = board[self.row - 1][self.column + 1]
                if piece.color != self.color:
                    self.valid_moves.append((self.row - 1, self.column + 1))
            elif self.color == Color.BLACK and isinstance(board[self.row + 1][self.column + 1], Piece):
                piece = board[self.row + 1][self.row + 1]
                if piece.color != self.color:
                    self.valid_moves.append((self.row + 1, self.column + 1))

        if self.column - 1 > 0:
            if self.color == Color.WHITE and isinstance(board[self.row - 1][self.column - 1], Piece):
                piece = board[self.row - 1][self.column - 1]
                if piece.color != self.color:
                    self.valid_moves.append((self.row - 1, self.column - 1))
            elif self.color == Color.BLACK and isinstance(board[self.row + 1][self.column - 1], Piece):
                piece = board[self.row + 1][self.column - 1]
                if piece.color != self.color:
                    self.valid_moves.append((self.row + 1, self.column - 1))








