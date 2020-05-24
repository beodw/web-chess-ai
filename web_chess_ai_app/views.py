from django.shortcuts import render
from .ai_module import chess_ai
import chess
from django.http import HttpResponse

# Landing page
def home(request):
	return render(request, 'web_chess_ai_app/chess_game.html', {})

# Returns ai move given a state fo the chess board
def play(request):
	fen = request.GET['fen']
	state = chess.Board(fen) # initialize a board state using fen
	move = chess_ai.minimax(state) #search through game tree using board to find best_move
	return HttpResponse(move.uci()) # return move as a uci string e.g. a2b4

	