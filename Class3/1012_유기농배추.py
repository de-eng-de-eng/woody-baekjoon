import sys
sys.setrecursionlimit(10000)

def replace(array: list, X: int, Y: int) -> None:
    array[Y][X] = 0

def search_all(array: list, X: int, Y: int) -> None:
    search_field = [(X-1, Y), (X+1, Y), (X, Y-1), (X, Y+1)]
    search = []
    
    for x, y in search_field:
        if x >= len(array[0]) or x < 0 or y >= len(array) or y < 0:
            pass
        else:
            search.append((x, y))

    if len(search) > 0:
        for x, y in search:
            try:
                if array[y][x] == 0:
                    pass
                else:
                    replace(array, x, y)
                    search_all(array, x, y)
                    pass
            except IndexError:
                pass


if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())
        
        field = [[0]*M for x in range(N)]
        earthworm = 0

        for _ in range(K):
            X, Y = map(int, input().split())
            field[Y][X] = 1
        
        for Y in range(N):
            for X in range(M):
                if field[Y][X] == 0:
                    pass
                else:
                    earthworm += 1
                    replace(field, X, Y)
                    search_all(field, X, Y)
        
        print(earthworm)


