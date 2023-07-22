import sys
from collections import defaultdict

fin_result = defaultdict(int)

for _ in range(10):

    quotient, remainder = divmod(
        int(sys.stdin.readline().strip()),
        42
    )
    
    fin_result[remainder] += 1

print(len(fin_result.keys()))