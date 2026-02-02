
from piece import PieceType

def input_parser(user_input):
    if len(user_input) != 5:
        print('Input must be 5 characters long')
        return

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
        piece = PieceType.PAWN
    else:
        raise Exception('First character must be R, N, B, Q, K, or P')

    str_columns = [user_input[1], user_input[3]]
    int_columns = []

    for column in str_columns:
        if column == 'A':
            int_columns.append(0)
        elif column == 'B':
            int_columns.append(1)
        elif column == 'C':
            int_columns.append(2)
        elif column == 'D':
            int_columns.append(3)
        elif column == 'E':
            int_columns.append(4)
        elif column == 'F':
            int_columns.append(5)
        elif column == 'G':
            int_columns.append(6)
        elif column == 'H':
            int_columns.append(7)
        else:
            raise Exception('Error in column input. Ensure use of A-H')

    if int(user_input[2]) < 1 or int(user_input[2]) > 8 or int(user_input[4]) < 1 or int(user_input[4]) > 8:
        raise Exception('Error in row input. Rows must be between 1 and 8')

    origin_column = int_columns[0]
    origin_row = 8 - int(user_input[2])
    new_column = int_columns[1]
    new_row = 8 - int(user_input[4])

    return piece, origin_column, origin_row, new_column, new_row
