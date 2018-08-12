import random
import os

# Draw Grid
# random location monster, player, door
# draw player on grid
# take input for movement
# move player, unless invalid(not out off grid)
# clear screen

CELLS = [(0,0), (1,0), (2,0),
		 (0,1), (1,1), (2,1),
		 (0,2), (1,2), (2,2)]

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
	return random.sample(CELLS,3)

def move_player(player, move):

	valid_moves = get_moves(player)

	if move in valid_moves:
		x, y = player
		if move == 'LEFT':
			x -= 1
		elif move == 'RIGHT':
			x += 1
		elif move == 'UP':
			y -= 1
		else:
			y+1

		player = x, y
		return player

	else:
		print ("Invalid Move")
		return player

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	x , y = player

	if x==0:
		moves.remove("LEFT")
	if x==2:
		moves.remove("RIGHT")
	if y==0:
		moves.remove("UP")
	if y==2:
		moves.remove("DOWN")

	return moves


monster, door, player = get_locations()
while True:
	print("Welcome to the Dungeon")
	print("You're currently in the room ", player)
	print("You can move ",get_moves(player))
	print("Enter QUIT to quit")

	move = input("> ").upper()


	if move == 'QUIT':
		break
	else:
		player = move_player(player,move)

	# Good move = change
	# Bad move = no change
	# Door = Victory
	# Monster = Death
	# otherwise loop again



