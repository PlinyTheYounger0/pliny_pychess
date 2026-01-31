
from input_parser import input_parser
from piece import Piece, Color, PieceType
from board import init_board, set_pieces, print_board, get_piece, update_pieces

def main():
    board = init_board()
    board = set_pieces(board)
    
    white_king = board[8][5]
    black_king = board[1][5]
    turn_color = 'White'

    print_board(board)
    update_pieces(board)

    while white_king.mated == False and black_king.mated == False:
        player_input = input(f'\nWhat is your move {turn_color}?: ')
        player_input = player_input.upper()

        if player_input == 'Q':
            break
        else:
            piece, origin_column, origin_row, new_column, new_row = input_parser(player_input)


        moving_piece, get_piece_exit_code = get_piece(board, piece, origin_column, origin_row)


        if get_piece_exit_code == 0:

            if turn_color == 'White' and moving_piece.color != Color.WHITE:
                print('\n***You cannot move a piece of the opposite color***\n')
            elif turn_color == 'Black' and moving_piece.color != Color.BLACK:
                print('\n***You cannot move a piece of the opposite color***\n')
            else:    
                moving_piece.check_valid_moves(board)
                '''
                print(moving_piece)
                print('Same Object?', board[origin_row][origin_column] == moving_piece)
                print('Moving Piece Row, Column', (moving_piece.row, moving_piece.column))
                '''
                print(moving_piece.valid_moves)


                new_board, move_exit_code = moving_piece.move(board, new_row, new_column)

                if move_exit_code == 0:
                    if moving_piece.piece_type == PieceType.KING:
                        if turn_color == 'White':
                            white_king = moving_piece
                        if turn_color == 'Black':
                            black_king = moving_piece

                    update_pieces(new_board)
                    white_king.king_in_check(new_board)
                    black_king.king_in_check(new_board)

                    print(white_king.in_check, white_king.row, white_king.column)
                    
                    if turn_color == 'White' and white_king.in_check == True:
                        print('\n***Invalid Move***\n***King in Check***')
                    elif turn_color == 'Black' and black_king.in_check == True:
                        print('\n***Invalid Move***\n***King in Check***')
                    else:
                        board = new_board
                        if turn_color == 'White':
                            turn_color = 'Black'
                        elif turn_color == 'Black':
                            turn_color = 'White'
                        
                    
                    update_pieces(board)
                    print_board(board)
    if white_king.mated == True:
        print('\n\n***!!!Black Wins!!!***\n\n')
    if black_king.mated == True:
        print('\n\n***!!!White Wins!!!***\n\n')
    
if __name__ == '__main__':
    main()
