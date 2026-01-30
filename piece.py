
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
        move = (new_row, new_column)
        old_column = self.column
        old_row = self.row

        if self.valid_moves:
            if move in self.valid_moves:
                board[new_row][new_column] = self
                self.column = new_column
                self.row = new_row
                board[old_row][old_column] = ' *'
                self.has_moved = True
            else:
                print('\n***Invalid Move***\n')
                return board, 1

        else:
            print('\n***Invalid Move***\n')
            return board, 1

        return board, 0
                

    def check_valid_moves(self, board):
        self.valid_moves = []
        directions = [ 
                    (0, -1),
                    (0, 1),
                    (-1, 0),
                    (1, 0),
                ]

        for direction_row, direction_column in directions:
            row = self.row + direction_row
            column = self.column + direction_column

            while 1 <= row <= 8 and 1 <= column <= 8:
                space = board[row][column]

                if isinstance(space, Piece):
                    if self.color != space.color:
                        self.valid_moves.append((self.row, column))
                    break 
                
                self.valid_moves.append((row, column))

                row += direction_row
                column += direction_column

class Knight(Piece):
    def __init__(self, row, column, Color, PieceType):
        super().__init__(row, column, Color, PieceType)
        
    def move(self, board, new_row, new_column):
            move = (new_row, new_column)
            old_column = self.column
            old_row = self.row

            if self.valid_moves:
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
        directions = [
                    (-2, 1),
                    (-2, -1),
                    (2, 1),
                    (2, -1),
                    (1, -2),
                    (-1, -2),
                    (1, 2),
                    (-1, 2),
                ]
        for direction_row, direction_column in directions:
            row = self.row + direction_row
            column = self.column + direction_column

            if 1 <= row <= 8 and 1 <= column <= 8:
                space = board[row][column]

                if isinstance(space, Piece):
                    if self.color != space.color:
                        self.valid_moves.append((row, column))
                    else:
                        continue

                self.valid_moves.append((row, column))

class Bishop(Piece):
    def __init__(self, row, column, Color, PieceType):
        super().__init__(row, column, Color, PieceType)

    def move(self, board, new_row, new_column):
        pass
'''
    def check_valid_moves(self, board):
        self.valid_moves = []
        count = 1
        
        for column in range(self.column + 1, 9):
            if self.row - count > 0:
                space = board[self.row - count][column]
                count += 1

                if isinstance(space, Piece):
                    if self.color == space.color:
                        break
                    else:
                        self.valid_moves.append((self.row - count, column))
                        break
                else:
                    self.valid_moves.append((self.row - count, column))

        count = 1

        for column in range(self.column - 1, 0, -1):
            if self.row - count > 0:
                space = board[self.row - count][column]
                count += 1

                if isinstance(space, Piece):
                    if self.color == space.color:
                        break
                    else:
                        self.valid_moves.append((self.row - count, column)
                        break
                else:
                    self.vald_moves.append((self.row - count, column))

        count = 1

        for column in range(self.column + 1, 9):
            if self.row + count < 9:
                space = board[self.row + count][column]
                count += 1
                
                if isinstance(space, Piece):
                    if self.color == space.color:
                        break
                    else:
                        self.valid_moves.append((self.row + count, column)
                        break   
                else:   
                    self.vald_moves.append((self.row + count, column))

        count = 1

        for column in range(self.column - 1, 0, -1):
            if self.row + count < 9:
                space = board[self.row + count][column]
                count += 1
                
                if isinstance(space, Piece):
                    if self.color == space.color:
                        break
                    else:
                        self.valid_moves.append((self.row + count, column)
                        break   
                else:   
                    self.vald_moves.append((self.row + count, column))
'''


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
        move = (new_row, new_column)
        old_column = self.column
        old_row = self.row

        if self.valid_moves:
            if move in self.valid_moves:
                board[new_row][new_column] = self
                self.column = new_column
                self.row = new_row
                board[old_row][old_column] = ' *'
                self.has_moved = True
        else:
            print('\n***Invalid Move***\n')
            return board, 1

        return board, 0

    def check_valid_moves(self, board):
        self.valid_moves = []


        if self.has_moved == False:

            if self.color == Color.WHITE:
                space_1 = board[self.row - 1][self.column]
                space_2 = board[self.row - 2][self.column]
                if not isinstance(space_1, Piece) and not isinstance(space_2, Piece):
                    self.valid_moves.append((self.row - 2, self.column))

            elif self.color == Color.BLACK:
                space_1 = board[self.row + 1][self.column]
                space_2 = board[self.row + 2][self.column]
                if not isinstance(space_1, Piece) and not isinstance(space_2, Piece):
                    self.valid_moves.append((self.row + 2, self.column))


        if self.color == Color.WHITE:
            if self.row - 1 > 0:
                space = board[self.row - 1][self.column]
                if not isinstance(space, Piece):
                    self.valid_moves.append((self.row - 1, self.column))

        elif self.color == Color.BLACK:
            space = board[self.row + 1][self.column]
            if not isinstance(space, Piece):
                self.valid_moves.append((self.row + 1, self.column))

                    
        if self.column + 1 < 9:

            if self.color == Color.WHITE:
                space = board[self.row -1][self.column + 1]
                if isinstance(space, Piece):
                    if space.color != self.color:
                        self.valid_moves.append((self.row - 1, self.column + 1))

            elif self.color == Color.BLACK:
                space = board[self.row + 1][self.row + 1]
                if isinstance(space, Piece):
                    if space.color != self.color:
                        self.valid_moves.append((self.row + 1, self.column + 1))


        if self.column - 1 > 0:

            if self.color == Color.WHITE:
                space = board[self.row - 1][self.column - 1]
                if isinstance(space, Piece):
                    if space.color != self.color:
                        self.valid_moves.append((self.row - 1, self.column - 1))

            elif self.color == Color.BLACK:
                space = board[self.row + 1][self.column - 1]
                if isinstance(space, Piece):
                    if space.color != self.color:
                        self.valid_moves.append((self.row + 1, self.column - 1))








