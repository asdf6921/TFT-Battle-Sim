# main.py
from character import Character
from combat import battle
from randBoard import generate_random_board
from board import Board

# Create the board and place characters
board1 = generate_random_board(3, 3, 5, "Red")
board2 = generate_random_board(3, 3, 5, "Blue")
combined_board = Board.combine_boards(board1, board2)
battle(combined_board)