import chess
import numpy

# The tables denote the points scored for the position of the chess pieces on the board.
PAWN_TABLE = numpy.array([
		[ 0,  0,  0,  0,  0,  0,  0,  0],
		[ 5, 10, 10,-20,-20, 10, 10,  5],
		[ 5, -5,-10,  0,  0,-10, -5,  5],
		[ 0,  0,  0, 20, 20,  0,  0,  0],
		[ 5,  5, 10, 25, 25, 10,  5,  5],
		[10, 10, 20, 30, 30, 20, 10, 10],
		[50, 50, 50, 50, 50, 50, 50, 50],
		[ 0,  0,  0,  0,  0,  0,  0,  0]
])

ROOK_TABLE = numpy.array([
		[ 0,  0,  0,  5,  5,  0,  0,  0],
		[-5,  0,  0,  0,  0,  0,  0, -5],
		[-5,  0,  0,  0,  0,  0,  0, -5],
		[-5,  0,  0,  0,  0,  0,  0, -5],
		[-5,  0,  0,  0,  0,  0,  0, -5],
		[-5,  0,  0,  0,  0,  0,  0, -5],
		[ 5, 10, 10, 10, 10, 10, 10,  5],
		[ 0,  0,  0,  0,  0,  0,  0,  0]
])

KNIGHT_TABLE = numpy.array([
		[-50, -40, -30, -30, -30, -30, -40, -50],
		[-40, -20,   0,   5,   5,   0, -20, -40],
		[-30,   5,  10,  15,  15,  10,   5, -30],
		[-30,   0,  15,  20,  20,  15,   0, -30],
		[-30,   5,  15,  20,  20,  15,   0, -30],
		[-30,   0,  10,  15,  15,  10,   0, -30],
		[-40, -20,   0,   0,   0,   0, -20, -40],
		[-50, -40, -30, -30, -30, -30, -40, -50]
])

QUEEN_TABLE = numpy.array([
		[-20, -10, -10, -5, -5, -10, -10, -20],
		[-10,   0,   5,  0,  0,   0,   0, -10],
		[-10,   5,   5,  5,  5,   5,   0, -10],
		[  0,   0,   5,  5,  5,   5,   0,  -5],
		[ -5,   0,   5,  5,  5,   5,   0,  -5],
		[-10,   0,   5,  5,  5,   5,   0, -10],
		[-10,   0,   0,  0,  0,   0,   0, -10],
		[-20, -10, -10, -5, -5, -10, -10, -20]
])

BISHOP_TABLE = numpy.array([
		[-20, -10, -10, -10, -10, -10, -10, -20],
		[-10,   5,   0,   0,   0,   0,   5, -10],
		[-10,  10,  10,  10,  10,  10,  10, -10],
		[-10,   0,  10,  10,  10,  10,   0, -10],
		[-10,   5,   5,  10,  10,   5,   5, -10],
		[-10,   0,   5,  10,  10,   5,   0, -10],
		[-10,   0,   0,   0,   0,   0,   0, -10],
		[-20, -10, -10, -10, -10, -10, -10, -20]
])


#Returns the best move given a current state of the board. Board must be chess.Board object.
def minimax(state): #Searches one level in the game tree
	highest_possible_score = 10000 # worst possible score for min i.e. +Infinite.
	for index, move in enumerate(state.legal_moves):
		
		state.push(move) #generate state (a child-node of current state)
		current_score = evaluate(state)
		# print(f'move {move.uci()} is current_move with score : {current_score}')

		if index == 0 or (lowest_score  > current_score): #if lowest or first state explored then best move is current move.
			# print(f'move {move.uci()}, with score : {current_score} is being inserted as best move')
			best_move = move
			lowest_score = current_score
			
		state.pop()	#return to initial state(parent-node)
	# print(f'selected move is : {best_move.uci()}')
	return best_move

def evaluate(state): #apply piece position and material heuristics to calculate score
	score = 0

	material = get_material_score(state)
	
	pawns = get_piece_position_score(state, chess.PAWN, PAWN_TABLE)
	knights = get_piece_position_score(state, chess.KNIGHT, KNIGHT_TABLE)
	bishops = get_piece_position_score(state, chess.BISHOP, BISHOP_TABLE)
	rooks = get_piece_position_score(state, chess.ROOK, ROOK_TABLE)
	queens = get_piece_position_score(state, chess.QUEEN, QUEEN_TABLE)

	return material + pawns + knights + bishops + rooks + queens	

def get_piece_position_score(state, piece_type, table):
		white = 0
		black = 0
		piece_map = state.piece_map() #Dict mapping pieces to square indeces {a1:0, b2:1, ... g8:63}.
		for square in piece_map:
			piece = piece_map[square]
			x = chess.square_file(square)
			y = chess.square_rank(square)
			if (piece.piece_type == piece_type):
				if (piece.color == chess.WHITE):
					white += table[x][y]
				else:
					black += table[7 - x][y]

		return white - black

def get_material_score(state): #compute material score for each side
	white = 0
	black = 0
	piece_map = state.piece_map() #Dict mapping pieces to square indeces a1 = 0, b2 = 1, ... g8 = 63.
	for square in piece_map:
		piece = piece_map[square]
		if (piece.color ==  chess.BLACK): #if black piece

			black += value(piece)
		else:
			white += value(piece)

	return white - black

def value(piece):
		symbol = piece.symbol()
		symbol = symbol.lower()
		if symbol == 'k':
			return 10000
		if symbol == 'q':
			return 9
		if symbol == 'r':
			return 5
		if symbol == 'b':
			return 3
		if symbol == 'n': 
			return 3
		if symbol == 'p':
			return 1  
		else:
			return 0

