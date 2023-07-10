import sys
from collections import deque

N = int(sys.stdin.readline().strip())
I = deque(sys.stdin.readline().strip().split())
v = sys.stdin.readline().strip()

print(I.count(v))