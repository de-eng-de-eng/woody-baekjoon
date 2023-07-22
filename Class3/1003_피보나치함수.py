import sys
from collections import deque, Counter

def fibonacci(counter: list, n: int) -> int:
    if n == 0:
        counter[0] += 1
        return 0
    elif n == 1:
        counter[1] += 1
        return 1
    else:
        return fibonacci(counter, n-1) + fibonacci(counter, n-2)

def fibonacci_memoization(n: int):
    fibo_deque = deque(
        [
            {0:1, 1:0},
            {0:0, 1:1}
        ]
    )
    
    for i in range(2, n+1):
        fibo_deque.append(
            {
                0: fibo_deque[i-1][0] + fibo_deque[i-2][0],
                1: fibo_deque[i-1][1] + fibo_deque[i-2][1]
            }
        )
    
    return(fibo_deque)

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    
    #fin_result = [0, 0]
    #fibonacci(fin_result, N)
    #print(fin_result[0], fin_result[1])

    result = fibonacci_memoization(N)
    print(result[-1][0], result[-1][1])