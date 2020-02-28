"""
This program is a command line Tic-Tac-Toe game which is made using a phenomenon called magic matrix.
"""
#player1 and player2 are the lists which keeps the record of the individual player's moves. 
player1 = []
player2 = []
#magic is that magical matrix which is used to check if any of the player have won the game.
magic = [2,7,6,9,5,1,4,3,8]
#board is used for the keeping track of the overall game.
board = ['_','_','_','_','_','_','_','_','_']
#game is used to control the iteration.
game = True
#player_inturn is used to keep track of the player whose turn it is.
player_inturn = 1
#won function is used to check if the player has won the game or not.
def won(lis):
	if sum(lis) == 15:
		return True
	else:
		return False
#when the elements of player1 and player2 lists contains 9 elements combined that means all of the 9 positions are explores(taken) so that game is tied. 
def draw(l1,l2):
	if len(l1) + len(l2) == 9:
		return True
#printboard is used to print the current situation of the board. 
def printboard(board):
	k= 0
	for i in range(3):
		for j in range(3):
			print(" | ",board[k]," | ",end="")
			k+=1
		print()
#initially print the board once: 
printboard(board)
#main Game logic
while game:
	print("Player-> ", player_inturn, "enter the move: ", end="")
	move = int(input())
	#if move does not exist in the range of 1 to 9 it is illegal
	if(move not in magic):
		print("Enter a legal move (1-9)")
		continue
	#main logic of the game
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