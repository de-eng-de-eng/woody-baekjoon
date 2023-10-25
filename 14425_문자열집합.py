import sys
from collections import defaultdict


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().strip().split())

    S = []
    for _ in range(N):
        S.append(input().strip())

    word_list = []
    for _ in range(M):
        word_list.append(input().strip())
    
    count = 0
    for word in word_list:
        if word in S:
            count += 1


    print(count)