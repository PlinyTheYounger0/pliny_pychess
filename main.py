
import sys
from input_parser import input_parser
from piece import Piece, Color
from board import init_board, set_pieces, print_board, get_piece

def main():
    board = init_board()
    board = set_pieces(board)
    
    white_king = board[8][5]
    black_king = board[1][5]
    turn_color = 'White'

    while white_king.mated == False and black_king.mated == False:
        print_board(board)

        player_input = input(f'What is your move {turn_color}?: ')
        player_input = player_input.upper()

        if player_input == 'Q':
            break
        else:
            piece, origin_column, origin_row, new_column, new_row = input_parser(player_input)


        if turn_color == 'White':
            turn_color = 'Black'
        elif turn_color == 'Black':
            turn_color = 'White'

if __name__ == '__main__':
    main()
