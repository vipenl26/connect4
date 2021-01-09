
def check(board):

    #straight combination

    for i in range(6):
        for j in range(4):
            if(board[i][j]=="R" and board[i][j+1]=="R" and board[i][j+2]=="R" and board[i][j+3]=="R"):
                return True
            if(board[i][j]=="Y" and board[i][j+1]=="Y" and board[i][j+2]=="Y" and board[i][j+3]=="Y"):
                return True
    
    #vertical combination

    for i in range(3):
        for j in range(7):
            if(board[i][j]=="R" and board[i+1][j]=="R" and board[i+2][j]=="R" and board[i+3][j]=="R"):
                return True
            if(board[i][j]=="Y" and board[i+1][j]=="Y" and board[i+2][j]=="Y" and board[i+3][j]=="Y"):
                return True
    
    #1st diagonal combination

    for i in range(3):
        for j in range(4):
            if(board[i][j]=="R" and board[i+1][j+1]=="R" and board[i+2][j+2]=="R" and board[i+3][j+3]=="R"):
                return True
            if(board[i][j]=="Y" and board[i+1][j+1]=="Y" and board[i+2][j+2]=="Y" and board[i+3][j+3]=="Y"):
                return True

    #2nd diagonal combination

    for i in range(3):
        for j in range(3,7):
            if(board[i][j]=="R" and board[i+1][j-1]=="R" and board[i+2][j-2]=="R" and board[i+3][j-3]=="R"):
                return True
            if(board[i][j]=="Y" and board[i+1][j-1]=="Y" and board[i+2][j-2]=="Y" and board[i+3][j-3]=="Y"):
                return True

    return False

def isDraw(board):
    cnt=0
    for i in range(7):
        if board[0][i]!="0":
            cnt+=1
    return cnt==7