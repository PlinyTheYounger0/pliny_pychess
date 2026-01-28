
from input_parser import input_parser
from piece import Piece, Color
from board import init_board, set_pieces, print_board, get_piece, update_pieces

def main():
    board = init_board()
    board = set_pieces(board)
    
    white_king = board[8][5]
    black_king = board[1][5]
    turn_color = 'White'

    while white_king.mated == False and black_king.mated == False:
        print_board(board)
        update_pieces(board)

        player_input = input(f'What is your move {turn_color}?: ')
        player_input = player_input.upper()

        if player_input == 'Q':
            break
        else:
            piece, origin_column, origin_row, new_column, new_row = input_parser(player_input)
        
        moving_piece = get_piece(board, piece, origin_column, origin_row)
        
        if turn_color == 'White' and moving_piece.color != Color.WHITE:
            print('\n***You cannot move a piece of the opposite color***\n')
        elif turn_color == 'Black' and moving_piece.color != Color.BLACK:
            print('\n***You cannot move a piece of the opposite color***\n')
        else:    
            moving_piece.check_valid_moves(board)
            print(moving_piece)
            print('Same Object?', board[origin_row][origin_column] == moving_piece)
            print('Moving Piece Row, Column', (moving_piece.row, moving_piece.column))
            print(moving_piece.valid_moves)
            board, move_exit_code = moving_piece.move(board, new_row, new_column)
        
        if turn_color == 'White' and move_exit_code == 0:
            turn_color = 'Black'
        elif turn_color == 'Black' and move_exit_code == 0:
            turn_color = 'White'

if __name__ == '__main__':
    main()
