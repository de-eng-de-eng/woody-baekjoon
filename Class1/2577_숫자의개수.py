import sys
from collections import Counter

fin_num = 1

def multiply(a: int, b: int) -> int:
    return a * b

for _ in range(3):
    fin_num = multiply(
        fin_num, int(sys.stdin.readline().strip())
        )

fin_result = Counter(str(fin_num))
for i in range(10):
    print(fin_result[str(i)])