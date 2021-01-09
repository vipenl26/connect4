from Check import check, isDraw
from copy import deepcopy
dic = dict()
swap = {"R": "Y", "Y": "R"}
def drop_coin(board,row,color):
	for i in range(5,-1,-1):
		if board[i][row]=="0":
			board[i][row]=color
			return board

def show(a):
	for i in a:
		print(*i)
	print("-----------")

def MiniMax(board,color,depth):
	mini=float('inf')
	maxi=-float('inf')
	if check(board):
		return dic[color]*-1
	elif isDraw(board):
		return 0
	elif depth==0:
		return 1
	for i in range(7):
		if board[0][i]!="0":
			continue
		board2=drop_coin(deepcopy(board),i,color)
		temp = MiniMax(board2,swap[color],depth-1)
		maxi=max(temp,maxi)
		mini=min(temp,mini)

	if dic[color]==1:
		return maxi
	else:
		return mini
		



def best_move(board,color,depth):
	global dic
	dic[color] = 1
	dic[swap[color]] = -1
	move = None
	score = -float('inf')
	for i in [3,4,2,5,1,6,0]:
		if board[0][i]!="0":
			continue
		board2 = drop_coin(deepcopy(board),i,color)
		current_score = MiniMax(board2,swap[color],depth)
		# print(current_score)

		if current_score > score:
			move = i
			score = current_score

	return move
