
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

        if self.valid_moves:
            if move in self.valid_moves:
                board[self.row][self.column] = '*"'
                self.column = new_column
                self.row = new_row
                board[self.column][row] = self
                self.has_moved = True
                return board, 0

        print('\n***Invalid Move***\n')
        return board, 1

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
                        self.valid_moves.append((row, column))
                    break 
                
                self.valid_moves.append((row, column))

                row += direction_row
                column += direction_column

class Knight(Piece):
    def __init__(self, row, column, Color, PieceType):
        super().__init__(row, column, Color, PieceType)
        
    def move(self, board, new_row, new_column):
            move = (new_row, new_column)

            if self.valid_moves:
                if move in self.valid_moves:
                    board[self.row][self.column] = '*"'
                    self.column = new_column
                    self.row = new_row
                    board[self.row][self.column] = self
                    return board, 0
            
            print('\n***Invalid Move***\n')
            return board, 1


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
        move = (new_row, new_column)

        if self.valid_moves:
            if move in self.valid_moves:
                board[self.row][self.column] = '*"'
                self.row = new_row
                self.column = new_column
                board[self.row][self.column] = self
                return board, 0

        print ('\n***Invalid Move***\n')
        return board, 1

    def check_valid_moves(self, board):
        self.valid_moves = []

        directions = [
                    (-1, 1),
                    (-1, -1),
                    (1, 1),
                    (1, -1),
                ]

        for direction_row, direction_column in directions:
            row = self.row + direction_row
            column = self.column + direction_column

            while 1 <= row <= 8 and 1 <= column <= 8:
                space = board[row][column]

                if isinstance(space, Piece):
                    if self.color != space.color:
                        self.valid_moves.append((row, column))
                    break

                self.valid_moves.append((row, column))

                row += direction_row
                column += direction_column

class Queen(Piece):
    def __init__(self, row, column, Color, PieceType):
        super().__init__(row, column, Color, PieceType)

    def move(self, board, new_row, new_column):
        move = (new_row, new_column)

        if self.valid_moves:
            if move in self.valid_moves:
                board[self.row][self.column] = '*"'
                self.row = new_row
                self.column = new_column
                board[self.row][self.column] = self
                return board, 0

        print('\n***Invalid Move***\n')
        return board, 1
    
    def check_valid_moves(self, board):
        self.valid_moves = []

        directions = [
                    (-1, 1),
                    (-1, 0),
                    (-1, -1),
                    (0, -1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                    (0, 1),
                ]

        for direction_row, direction_column in directions:
            row = self.row + direction_row
            column = self.column + direction_column

            while 1 <= row <= 8 and 1 <= column <= 8:
                space = board[row][column]

                if isinstance(space, Piece):
                    if self.color != space.color:
                        self.valid_moves.append((row, column))
                    break

                self.valid_moves.append((row, column))

                row += direction_row
                column += direction_column

class King(Piece):
    def __init__(self, row, column, Color, PieceType, has_moved=False, in_check=False, mated=False):
        super().__init__(row, column, Color, PieceType)
        self.has_moved = False
        self.in_check = False
        self.mated = False

    def move(self, board, new_row, new_column):
        move = (new_row, new_column)
        left_castle_moves = [(8, 3), (1, 3)]
        right_castle_moves = [(8, 7), (1, 7)] 

        if self.valid_moves:
            if move in self.valid_moves:
                if self.has_moved == False:

                    if move in left_castle_moves:
                        board[self.row][self.column] = '*"'
                        self.row = new_row
                        self.column = new_column
                        board[self.row][self.column] = self

                        rook = board[new_row][1]
                        board[rook.row][rook.column] = '*"'
                        rook.column = 4
                        board[rook.row][rook.column] = rook

                    if move in right_castle_moves:
                        board[self.row][self.column] = '*"'
                        self.column = new_column
                        board[self.row][self.column] = self

                        rook = board[new_row][8]
                        board[rook.row][rook.column] = '*"'
                        rook.column = 6
                        board[rook.row][rook.column] = rook

                board[self.row][self.column] = '*"'
                self.row = new_row
                self.column = new_column
                board[self.row][self.column] = self
                self.has_moved = True
                return board, 0

        print('\n***Invalid Move***\n')
        return board, 1

    def check_valid_moves(self, board):
        self.valid_moves = []

        directions = [
                    (-1, 1),
                    (-1, 0),
                    (-1, -1),
                    (0, -1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                    (0, 1),
                ]

        for direction_row, direction_column in directions:
            row = self.row + direction_row
            column = self.column + direction_column
            if 1 <= row <= 8 and 1 <= column <= 8: 
                space = board[row][column]

                if isinstance(space, Piece):
                    if self.color != space.color:
                        self.valid_moves.append((row, column))

                self.valid_moves.append((row, column))
        
        if self.in_check == False and self.has_moved == False:
            left_pieces = 0
            right_pieces = 0
            white_right_rook = board[8][8]
            white_left_rook = board[8][1]
            black_right_rook = board[1][8]
            black_left_rook = board[1][1]

            for column in range(2, 5):
                space = board[self.row][column]

                if isinstance(space, Piece):
                    left_pieces += 1
            
            for column in range(6, 8):
                space = board[self.row][column]
                
                if isinstance(space, Piece):
                    right_pieces += 1

            if left_pieces == 0:
                if self.color == Color.WHITE and white_left_rook.has_moved == False:
                    self.valid_moves.append((8, 3))
                elif self.color == Color.BLACK and black_left_rook.has_moved == False:
                    self.valid_moves.append((1, 3))

            if right_pieces == 0:
                if self.color == Color.WHITE and white_right_rook.has_moved == False:
                    self.valid_moves.append((8,7))
                elif self.color == Color.BLACK and black_right_rook.has_moved == False:
                    self.valid_moves.append((1, 7))

        if self.in_check == True and not self.valid_moves:
            self.mated = True


    def king_in_check(self, board):
        
        for row in range(1, 9):
            for column in range(1, 9):
                space = board[row][column]

                if isinstance(space, Piece):
                    if self.color != space.color:
                        if (self.row, self.column) in space.valid_moves:
                            self.in_check = True
        self.in_check = False

class Pawn(Piece):
    def __init__(self, row, column, Color, PieceType, has_moved=False):
        super().__init__(row, column, Color, PieceType)
        self.has_moved = False

    def move(self, board, new_row, new_column):
        move = (new_row, new_column)

        if self.valid_moves:
            if move in self.valid_moves:
                board[self.row][self.column] = '*"'
                self.column = new_column
                self.row = new_row
                board[self.row][self.column] = self
                self.has_moved = True
                return board, 0

        print('\n***Invalid Move***\n')
        return board, 1

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








