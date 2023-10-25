import sys


def DFS(node, edge, root):
    result = []
    return result


def BFS(node, edge, root):
    result = []
    return result



def main():
    global nodes, edges, V
    dfs_result = DFS(nodes, edges, V)
    bfs_result = BFS(nodes, edges, V)


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M, V = map(int, input().strip().split())

    nodes = [i for i in range(1,N+1)]
    edges = []

    for _ in range(M):
        edges.append(list(map(int, input().strip().split())))

    main()