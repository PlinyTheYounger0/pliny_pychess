
from piece import PieceType

def input_parser(user_input):
    if len(user_input) != 5:
        raise ValueError('Input must be 5 characters long')

    piece_var = user_input[0]

    if piece_var == 'R':
        piece = PieceType.ROOK
    elif piece_var == 'N':
        piece = PieceType.KNIGHT
    elif piece_var == 'B':
        piece = PieceType.BISHOP
    elif piece_var == 'Q':
        piece = PieceType.QUEEN
    elif piece_var == 'K':
        piece = PieceType.KING
    elif piece_var == 'P':
        piece = Piecetype.PAWN
    else:
        raise Exception('First character must be R, N, B, Q, K, or P')

    columns = [user_input[1], user_input[3]]

    for column in columns:
        if column == 'A':
            column = 1
        elif column == 'B':
            column = 2
        elif column == 'C':
            column = 3
        elif column == 'D':
            column = 4
        elif column == 'E':
            column = 5
        elif column == 'F':
            column = 6
        elif column == 'G':
            column = 7
        elif column == 'H':
            column = 8
        else:
            raise Exception('Error in column input. Ensure use of A-H')

    if user_input[2] < 1 or user_input[2] > 8 or user_input[4] < 1 or user_input[4] > 8:
        raise Exception('Error in row input. Rows must be between 1 and 8')

    origin_column = columns[0]
    orgin_row = user_input[2]
    new_column = columns[1]
    new_row = user_input[4]

    return piece, origin_column, origin_row, new_column, new_row
