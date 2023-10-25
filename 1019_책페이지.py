import sys
from math import log10, trunc
from collections import Counter

# Under 10^3
def calc():
    global N
    results = Counter()
    
    for i in map(str, range(1, N+1)):
        results.update(i)
    
    return results

def calc_mod(start, end):
    results = Counter()
    
    for i in map(str, range(start, end+1)):
        results.update(i)
    
    return results

# Pattern of number, 10^n (n>=3)
def pattern(n):
    result = {
        '0':pattern_zero(n),
        '1':n*pow(10, n-1)+1,
        '2':n*pow(10, n-1),
        '3':n*pow(10, n-1),
        '4':n*pow(10, n-1),
        '5':n*pow(10, n-1),
        '6':n*pow(10, n-1),
        '7':n*pow(10, n-1),
        '8':n*pow(10, n-1),
        '9':n*pow(10, n-1)
    }
    return Counter(result)

# Pattern of 0, 10^n (n>=3)
def pattern_zero(n):
    return int("{}{}{}".format(n-2, pow(10,n-2) - int("1"*(n-2)), n-1))


def main():
    global n, start, end
    
    if n < 3:
        return calc()
    elif n == 9:
        return pattern(n)
    elif n >= 3 and n < 9:
        patterns = pattern(n)
        remains = calc_mod(start, end)
        return patterns + remains
    
if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    n = trunc(log10(N))
    start = pow(10, n)+1
    end = N

    results = main()

    result = ""
    for i in range(10):
        result += "{} ".format(results[str(i)])

    print(result.strip())