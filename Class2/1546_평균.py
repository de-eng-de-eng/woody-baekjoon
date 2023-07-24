import sys
from decimal import Decimal

N = int(sys.stdin.readline().strip())
scores = list(map(float, sys.stdin.readline().strip().split()))

M = max(scores)

scores_new = list(map(lambda score: Decimal(score)/Decimal(M)*100, scores))

print(Decimal(sum(scores_new)) / Decimal(len(scores_new)))