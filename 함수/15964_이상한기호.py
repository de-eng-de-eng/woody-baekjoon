import sys

A, B = map(int, sys.stdin.readline().strip().split())

def CalAB(A, B):
    return (A+B)*(A-B)

print(CalAB(A, B))