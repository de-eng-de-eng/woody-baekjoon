import sys





if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().strip().split())
    
    items_w = []
    items_v = []
    for _ in range(N):
        W, V = map(int, input().strip().split())

        items_w.append(W)
        items_v.append(V)

        