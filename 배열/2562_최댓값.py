import sys
from collections import deque

A = deque([])

for _ in range(9):
    A.append(int(sys.stdin.readline().strip()))

print(max(A))
print(A.index(max(A)))