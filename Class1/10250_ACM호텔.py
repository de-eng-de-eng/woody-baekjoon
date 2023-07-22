
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    
    H, W, N = map(int, sys.stdin.readline().strip().split())
    
    room, floor = divmod(N, H)
    if floor == 0: # 꼭대기층
        if room in range(1,10):
            result = "{}0{}".format(str(H), str(room))
        else:
            result = "{}{}".format(str(H), str(room))
    else:
        if room in range(1,9):
            result = "{}0{}".format(str(floor), str(room+1))
        else:
            result = "{}{}".format(str(floor), str(room+1))

    print(result)