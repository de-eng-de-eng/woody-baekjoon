import sys


def make_array(N: int) -> list:
    return [[0]*pow(2,N) for x in range(pow(2,N))]


def search_z(N) -> None:
    global count, position, r, c

    count += 1
    
    if position == [r, c]:
        print(position, count)
    else:
        

        return search_Z(N-1)



if __name__ == "__main__":
    input = sys.stdin.readline()

    N, r, c = map(int, input.strip().split())

    A = make_array(N)

    count = 0
    position = [0, 0]

    search_z(N)