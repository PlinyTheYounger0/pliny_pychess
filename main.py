
from piece import Piece
from board import init_board, set_pieces

def main():
    board = init_board()
    board = set_pieces(board)

    for row in board:
        print(*(item.rep if isinstance(item, Piece) else item for item in row))

if __name__ == '__main__':
    main()
