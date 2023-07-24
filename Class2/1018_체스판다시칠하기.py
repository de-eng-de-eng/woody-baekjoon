import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
search = (range(N-8+2), range(M-8+2))
print(search)


orig_board = list()

for _ in range(N):
    row = sys.stdin.readline().strip()
    orig_board.append(list(row))

for i in search[0]:
    for j in search[1]:
        chess_board = []
        for x in range(i,i+8+1):
            chess_board.append(orig_board[i][j:j+8])
        
        print(chess_board)



def re_paint(x: int, y: int) -> int:
    changed = 0
    try:
        board[x-1][y]
    except: pass
    try:
        board[x+1][y]
    except: pass
    try: 
        board[x][y-1]
    except: pass
    try: 
        board[x][y+1]
    except: pass

    return changed