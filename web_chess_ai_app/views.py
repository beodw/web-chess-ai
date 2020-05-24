from django.shortcuts import render
from .ai_module import chess_ai
import chess

# Landing page
def home(request):
	return render(request, 'web_chess_ai_app/chess_game.html', {})

# Returns ai move given a state fo the chess board
def play(request):
	state = chess.Board()
	move = chess_ai.minimax(state)
	print(move)
	return render(request, 'web_chess_ai_app/chess_game.html', {})

	