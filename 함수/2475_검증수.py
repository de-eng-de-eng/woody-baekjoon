import sys

uniq_nums = map(
    lambda x: int(x)*int(x),
    sys.stdin.readline().strip().split()
)

print( sum(uniq_nums) % 10 )