import sys
from collections import deque

N, X = map(int, sys.stdin.readline().strip().split())
A = deque(sys.stdin.readline().strip().split())

lower_nums = ""
for item in A:
    if int(item) < X:
        lower_nums += "{} ".format(item)

print(lower_nums.strip())