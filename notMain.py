import Check
board=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]



def show():
    global board
    for i in board:
        print(*i)
        print("-------------------")


def Turn(color,row):
    global board
    for i in range(1,8):
        if board[-i][row]==0:
            board[-i][row]=color
            break

show()
while(Check.check(board)==False):
    choice= input().split(" ")
    Turn(choice[0],int(choice[1]))
    show()


print("LES goooo !!!!!!!!! We have a winner")


