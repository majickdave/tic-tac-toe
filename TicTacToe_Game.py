# -*- coding: utf-8 -*-
# David Samuel <--- Your name
# MSDS 7330 401 <--- Your section
# hello_world.py <--- File name
# 16 Jan 2016 <--- Date
LINE = "-------------"
X = "X"
O = "O"
NIL = " "
DRAW = "DRAW"

def print_instructions():
    print(
    """
          Welcome to Tic Tac Toe
                
                 0 | 1 | 2
               -------------
                 3 | 4 | 5
               -------------
                 6 | 7 | 8     
                 
         Player 1 is X and goes first
         Player 2 is O and goes second 
    """
    )

def game_letters():
    player1 = X
    player2 = O

    return player1, player2
    
def new_board():
    board = []
    for cell in range(9):
        board.append(NIL)
    return board

def show_board(board):
    print "\n", "  "+board[0], "|", board[1], "|", board[2] 
    print LINE
    print "  "+board[3], "|", board[4], "|", board[5] 
    print LINE
    print "  "+board[6], "|", board[7], "|", board[8] 

def winner(board):
    WINNING_TRIPLETS = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # 3 rows 
                       (0, 3, 6), (1, 4, 7), (2, 5, 8),   # 3 columns 
                       (0, 4, 8), (2, 4, 6))              # 2 diagonals 

    for row in WINNING_TRIPLETS:
        if board[row[0]] == board[row[1]] == board[row[2]] != NIL:
            winner = board[row[0]]
            return winner
    if NIL not in board:
        return DRAW
    return None


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def player_move(board, player1, player2):
    move = None
    while move not in legal_moves(board):
        move = ask_number("\nChoose a cell, (0 - 8):", 0, 9)
        if move not in legal_moves(board):
            print("\nThat cell is already taken.  Choose another.\n")
    return move

def next_turn(turn):
    """change turns from X to O"""
    if turn == X:
        return O
    else:
        return X

def legal_moves(board):
    moves = []
    for cell in range(9):
        if board[cell] == NIL:
            moves.append(cell)
    return moves

def message_winner(the_winner, player1, player2):

    if the_winner == player1:
        print("\nPlayer 1 Wins!")

    elif the_winner == player2:
        print("\nCongrats Player 2, you are smart!")

    elif the_winner == DRAW:
        print("\nThe result of the game was a draw...")
              
def main():

    print_instructions()
    player1, player2 = game_letters()
    turn = X
    board = new_board()
    show_board(board)

    while not winner(board):
        if turn == player2:
            move = player_move(board, player1, player2)
            board[move] = player2
        else:
            move = player_move(board, player1, player2)
            board[move] = player1
        show_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    message_winner(the_winner, player1, player2)


# start program
main()
input("\n\nPress the enter key to quit.")
    

   
    
    
