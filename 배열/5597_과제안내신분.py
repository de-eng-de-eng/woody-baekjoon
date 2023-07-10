import sys
from collections import deque

students = deque(range(1,31))

for _ in range(28):
    submit = int(sys.stdin.readline().strip())
    students.remove(submit)

for item in students:
    print(item)