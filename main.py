
import sys
from input_parser import input_parser
from piece import Piece
from board import init_board, set_pieces

def main():
    board = init_board()
    board = set_pieces(board)
    
    white_king = board[8][5]
    black_king = board[1][5]

    while white_king.mated == False and black_king.mated == False:
        for row in board:
            print(*(item.rep if isinstance(item, Piece) else item for item in row))

        player_input = input('What is your move?: ')
        player_input = player_input.upper()

        if player_input == 'Q':
            break
        else:
            piece, origin_pos, new_pos = input_parser(player_input)

if __name__ == '__main__':
    main()
