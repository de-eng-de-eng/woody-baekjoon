import sys

def re_paint(in_array: list, x: int, y: int) -> None:
    global count
    if in_array[x][y] == "W":
        in_array[x][y] = "B"
    elif in_array[x][y] == "B":
        in_array[x][y] = "W"
    count += 1
    
def check_color(in_array: list, x: int, y: int) -> None:
    if in_array[x][y] == in_array[x][y-1]:
        re_paint(in_array, x, y)

def search(in_array: list) -> None:
    ini_color = in_array[0][0]

    for i in range(len(in_array)):
        if i == 0:
            ini_color = in_array[i][0]
        else:                
            if ini_color == in_array[i][0]:
                re_paint(in_array, i, 0)
            ini_color = in_array[i][0]
        for j in range(1,len(in_array[i])):
            check_color(in_array, i, j)

if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().strip().split())
    chess_range = (range(N-8+1), range(M-8+1))

    orig_board = list()

    for _ in range(N):
        row = sys.stdin.readline().strip()
        orig_board.append(list(row))

    counts = []

    for i in chess_range[0]:
        for j in chess_range[1]:

            chess_board = []
            for x in range(i, i+8):
                chess_board.append(orig_board[x][j:j+8])            
            
            count = 0
            search(chess_board)
            counts.append(count)

    print(min(counts))