import os, signal
import subprocess
from subprocess import call, Popen, PIPE
import time
import chess
import random
import chess.pgn
import chess.svg
import sys

folder_path = "/home/duarte/Remember_the_position/Games"
files = os.listdir(folder_path)
random_file = random.choice(files)
file_path = os.path.join(folder_path, random_file)
pgn = open(file_path)
first_game = chess.pgn.read_game(pgn)


games = []
while first_game is not None:
    games.append(first_game)
    first_game = chess.pgn.read_game(pgn)

game = random.choice(games)

board = game.board()
for move in game.mainline_moves():
    board.push(move)

svg = chess.svg.board(board=board)
with open("chess_position.svg", "w") as file:
    file.write(svg)
command = ['eog', 'chess_position.svg']
subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


pieces_position = []
for piece_type in chess.PIECE_TYPES:
    for square in board.pieces(piece_type, chess.WHITE):
        pieces_position.append("{}{}".format(chess.PIECE_SYMBOLS[piece_type], chess.SQUARE_NAMES[square]))
    for square in board.pieces(piece_type, chess.BLACK):
        pieces_position.append("{}{}".format(chess.PIECE_SYMBOLS[piece_type], chess.SQUARE_NAMES[square]))

correct_answers = len(pieces_position)

print("You have 10 seconds to look at the board.")
for i in range(10, 0, -1):
    print("Remaining time: {} seconds.".format(i))
    time.sleep(1)
time.sleep(10)

subprocess.Popen(['pkill', 'eog'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Enter the pieces positions")
while correct_answers > 0:
    try:
        user_input = input()
    except EOFError:
        sys.exit()
    if user_input.lower() in pieces_position:
        print("Correct!")
        correct_answers -= 1
    else:
        print("Incorrect.")

if correct_answers == 0:
    print("You got all positions correct!")
