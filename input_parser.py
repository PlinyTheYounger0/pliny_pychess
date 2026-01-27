
from piece import PieceType

def input_parser(user_input):
    if len(user_input) != 5:
        raise ValueError('Input must be 5 characters long')

    if not isinstance(user_input[0], str):
        raise ValueError('First character of input (piece) must be a single letter')
    if not isinstance(user_input[1], str):
        raise ValueError('Second character of input (column) must be a single letter')
    if not isinstance(user_input[2], int):
        raise ValueError('Third character of input (row) must be an int')
    if not isinstance(user_input[3], str):
        raise ValueError('Fourth character of input (column) must be a single letter')
    if not isinstance(user_input[4], int):
        raise ValueError('Fifith character of input (row) must be an int')

    piece_var = user_input[0]
    origin_pos = (user_input[1], user_input[2])
    new_pos = (user_input[3], user_input[4])

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

    return piece, origin_pos, new_pos
