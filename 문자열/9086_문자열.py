import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    line = sys.stdin.readline().strip()
    print("{}{}".format(line[0], line[-1]))