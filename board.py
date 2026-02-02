
import copy
from piece import (
        Piece,
        PieceType, 
        Color, 
        Rook,
        Knight,
        Bishop,
        Queen,
        King,
        Pawn
        )

def init_board():
    
    rows = 8
    columns = 8
    new_space = '*"'
    board = []

    for i in range(rows):
        new_row = []
        for j in range(columns):
            new_row.append(new_space)
        board.append(new_row)
    
    return board


def set_pieces(board):
    pieces = []
    back_rank = [
            (Rook, PieceType.ROOK),
            (Knight, PieceType.KNIGHT),
            (Bishop, PieceType.BISHOP),
            (Queen, PieceType.QUEEN),
            (King, PieceType.KING),
            (Bishop, PieceType.BISHOP),
            (Knight, PieceType.KNIGHT),
            (Rook, PieceType.ROOK),
            ]

    for column, (piece, piece_type) in enumerate(back_rank, start = 0):
          pieces.extend([
                piece(7, column, Color.WHITE, piece_type),
                Pawn(6, column, Color.WHITE, PieceType.PAWN),
                piece(0, column, Color.BLACK, piece_type),
                Pawn(1, column, Color.BLACK, PieceType.PAWN),
            ])


    for piece in pieces:
        row = piece.row
        column = piece.column
        board[row].pop(column)
        board[row].insert(column, piece)
    
    return board

def get_piece(board, piece_type, origin_column, origin_row):
    piece = board[origin_row][origin_column]

    if not isinstance(piece, Piece):
        print('\nNo piece at origin position. Please try a different position\n')
        return None, 1
    elif piece.piece_type != piece_type:
        print('\nThere is not the piece you sought at that position\n')
        return None, 1
    else:
        return piece, 0

def print_board(board):

    print_board = copy.deepcopy(board)

    column_header = [' ', 'A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ']
    row_header = [1, 2, 3, 4, 5, 6, 7, 8]

    print_board.insert(0, column_header)
    print_board.append(column_header)

    for i in range(len(print_board)):
        if i in row_header:
            row_number_header = 9 - i
            print_board[i].insert(0, row_number_header)
            print_board[i].append(row_number_header)

    for row in print_board:
        print(*(item.rep if isinstance(item, Piece) else item for item in row))

def update_pieces(board):
    for row in range(0, 8):
        for column in range(0,8):
            space = board[row][column]
            if isinstance(space, Piece):
                space.check_valid_moves(board)
                space.row = row
                space.column = column
            else:
                continue











