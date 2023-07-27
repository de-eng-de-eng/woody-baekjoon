import sys

sys.setrecursionlimit(10000)

def change_item(A, idx1, idx2):
    global change, K

    A[idx1], A[idx2] = A[idx2], A[idx1]

    change += 1
    if change == K:
        a = min([A[idx1], A[idx2]])
        b = max([A[idx1], A[idx2]])
        print("{} {}".format(a, b))
        sys.exit()

def quick_sort(A, start, end):
    if start < end:
        q = partition(A, start, end)
        quick_sort(A, start, q-1)
        quick_sort(A, q+1, end)

def partition(A, start, end):
    x = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] <= x:
            i += 1
            change_item(A, i, j)
            #A[i], A[j] = A[j], A[i]

    if i+1 != end:
        change_item(A, i+1, end)
        #A[i+1], A[end] = A[end], A[i+1]
    return i+1

if __name__ == '__main__':
    line = sys.stdin.readline

    N, K = map(int, line().strip().split())
    A = list(map(int, line().strip().split()))

    change = 0
    quick_sort(A, 0, N-1)
    print(-1)