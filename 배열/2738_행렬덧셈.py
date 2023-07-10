import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

A, B = deque([]), deque([])
for _ in range(N):
    A.append(deque(sys.stdin.readline().strip().split()))
for _ in range(N):
    B.append(deque(sys.stdin.readline().strip().split()))

C = []
for i in range(N):
    C.append([str(int(x)+int(y)) for x, y in zip(A[i], B[i])])

for item in C:
    print(" ".join(item))