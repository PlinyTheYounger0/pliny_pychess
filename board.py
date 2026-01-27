
from piece import (
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
    new_space = ' *'
    board = [[' ',' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H']]

    for i in range(rows):
        new_row = []
        new_row.append(rows - i)
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
            (Rook, PieceType.ROOK),
            (Knight, PieceType.KNIGHT),
            (Bishop, PieceType.BISHOP),
            ]

    for column, (piece, piece_type) in enumerate(back_rank, start = 1):
          pieces.extend([
                piece(8, column, Color.WHITE, piece_type),
                Pawn(7, column, Color.WHITE, PieceType.PAWN),
                piece(1, column, Color.BLACK, piece_type),
                Pawn(2, column, Color.BLACK, PieceType.PAWN),
            ])


    for piece in pieces:
        row = piece.row
        column = piece.column
        board[row].pop(column)
        board[row].insert(column, piece)
    
    return board
