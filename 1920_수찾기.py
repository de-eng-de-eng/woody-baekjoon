import sys
from bisect import bisect_left, bisect_right


def binary_search(array, x):
    idx = bisect_left(array, x)
    return idx < len(array) and array[idx] == x


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    arrA = list(map(int, input().strip().split()))
    M = int(input().strip())
    arrM = list(map(int, input().strip().split()))

    arrA.sort()

    for item in arrM:
        if binary_search(arrA, item):
            print(1)
        else:
            print(0)
