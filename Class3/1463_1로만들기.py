import sys


def calculator(X: int, m: int, n: int, l: int) -> int:
    N = pow(3, m) * pow(2, n) - pow(1, l)


def make_one(X):
    if X == 1:
        return X
    else:
        X = calculator(X)
        return make_one(X)


if __name__ == "__main__":
    input = sys.stdin.readline()

    N = int(input.strip())

    count = 0
    
    make_one(N)

    print(count)