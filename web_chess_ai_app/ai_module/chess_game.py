import chess
import chess.svg
import chess.engine
import chess_ai

"""
chess game alg:
1.Initialize game
2.set chess.turn to WHITE
3.while not is_game_over():
	move = player_input
	if is_legal(move):
		push(move)
		change_turn(chess.turn)
	else:
		print('illegal move')

4.game_over() 

"""

def get_player_input():
	"""
	interfaces with GUI modules to get player input and return a move
	"""
	#Get move from player
	print('Make a move')
	from_square = input('From_square: ')
	to_square = input('To_square: ')

	#Parse move into sqaure indeces
	square_indeces = get_move_squares(from_square.lower(), to_square.lower())

	#Generate move from indeces
	move = chess.Move(from_square=square_indeces[0], to_square=square_indeces[1])
	return move

def get_move_squares(from_square, to_square):
	try:
		squares = [from_square, to_square] #list to hold int values of squares as defined in the py-chess docs.
		indeces = []
		file_index = 0
		rank_index = 0

		for square in squares:
			for file in chess.FILE_NAMES:
				if file == square[0]:#if file matches input
					file_index = chess.FILE_NAMES.index(file)
					break

			rank_index = int(square[1]) - 1 
		
			square_int = chess.square(file_index=file_index, rank_index=rank_index)
			indeces.append(square_int)

		return indeces

	except Exception as e:
		print('invalid input. Enter a file-rank pairs e.g. A2 or b5 \n')
		move = get_player_input()
		indeces = [move.from_square, move.to_square]

		return indeces

def game_over(turn, result):
	"""
	Display winner using GUI.
	Give option to restart game.
	if resart:
		initialize game
	"""
	winner = change_turns(turn)
	print('results \n' + result)
	response = input('Play Again? Y or N : ')
	# response = user_input from GUI
	if response == 'Y':
		run_game()

def change_turns(turn):

	if turn == chess.WHITE:

		turn == chess.BLACK

	if turn == chess.BLACK:

		turn == chess.WHITE

	return turn

def run_game():

	#1. Initialize board and set white turn
	board = chess.Board()
	board.turn = chess.WHITE

	# main game loop
	# Note:  if either player or engine makes no move remember to change the current value of move to null.
	# Otherwise the previous value will be evaluated as the current move.
	while not board.is_game_over(): #check for end game condition
		print(f'{board} \n=======next_move========')
		if board.turn == chess.WHITE:
			print('player')
			move = get_player_input()
			
		else:
			# move = ChessAi.minimax(board)
			move = chess_ai.minimax(board)
			print('chess engine')
		if board.is_legal(move): #validate move and play if legal
			board.push(move)
			board.turn = change_turns(board.turn)
		else:
			print('illegal move')

	game_over(board.turn, board.result())

#start
run_game()









