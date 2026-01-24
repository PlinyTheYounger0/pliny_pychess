
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

    for i in range(1, 9):
        if i == 1 or i == 8:
            white_piece_1 = Rook(8, i, Color.WHITE, PieceType.ROOK)
            white_piece_2 = Pawn(7, i, Color.WHITE, PieceType.PAWN)
            black_piece_1 = Rook(1, i, Color.BLACK, PieceType.ROOK)
            black_piece_2 = Pawn(2, i, Color.BLACK, PieceType.PAWN)
        if i == 2 or i == 7:
            white_piece_1 = Knight(8, i, Color.WHITE, PieceType.KNIGHT)
            white_piece_2 = Pawn(7, i, Color.WHITE, PieceType.PAWN)
            black_piece_1 = Knight(1, i, Color.BLACK, PieceType.KNIGHT)
            black_piece_2 = Pawn(2, i, Color.BLACK, PieceType.PAWN)

        if i == 3 or i == 6:
            white_piece_1 = Bishop(8, i, Color.WHITE, PieceType.BISHOP)
            white_piece_2 = Pawn(7, i, Color.WHITE, PieceType.PAWN)
            black_piece_1 = Bishop(1, i, Color.BLACK, PieceType.BISHOP)
            black_piece_2 = Pawn(2, i, Color.BLACK, PieceType.PAWN)

        pieces.append(white_piece_1)
        pieces.append(white_piece_2)
        pieces.append(black_piece_1)
        pieces.append(black_piece_2)

    for piece in pieces:
        row = piece.row
        column = piece.column
        board[row].pop(column)
        board[row].insert(column, piece)
    
    return board
