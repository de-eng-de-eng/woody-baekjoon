import sys
from collections import deque

def fibonacci_memoization(n: int) -> deque:
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
    
    result = fibonacci_memoization(N)
    print(result[N][0], result[N][1])