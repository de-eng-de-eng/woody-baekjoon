import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    
    H, W, N = map(int, sys.stdin.readline().strip().split())
    
    rooms = []
    for room in range(1, W+1):
        for floor in range(1, H+1):
            if room < 10:
                rooms.append("{}0{}".format(floor, room))
            else:
                rooms.append("{}{}".format(floor, room))
    print(rooms[N-1])