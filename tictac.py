player1 = []
player2 = []
magic = [2,7,6,9,5,1,4,3,8]
board = ['_','_','_','_','_','_','_','_','_']
game = True
player_inturn = 1

def won(lis):

	if sum(lis) == 15:
		return True
	else:
		return False

def draw(l1,l2):
	if len(l1) + len(l2) == 9:
		return True


def printboard(board):
	k= 0
	for i in range(3):
		for j in range(3):
			print(" | ",board[k]," | ",end="")
			k+=1
		print()

printboard(board)

while game:
	

	print("Player-> ", player_inturn, "enter the move: ", end="")
	
	move = int(input())
	
	if(move not in magic):
		print("Enter a legal move (1-9)")
		continue
	
	if player_inturn==1:
		player1.append(magic[move-1])

		
		if(any(item in player1 for item in player2)):
			print("Illegal------------!")
			continue
		board[move-1] = 'O'

		if(won(player1)):
			print("\n\nCongrats Player 1 won the game\n\n")
			game = False
		
		player_inturn = 2
	
	else:
		player2.append(magic[move-1])
		
		if(any(item in player1 for item in player2)):
			print("Illegal------------!")
			continue
		board[move-1] = 'X'
		if(won(player2)):
			print("\n\nCongrats Player 2 won the game\n\n")
			game = False
		
		player_inturn = 1

	if(draw(player1,player2)):
		print("Game is tied: ")
		game = False

	print("Board::::::::::")
	printboard(board)
	print(":::::::::::::::")

	