import sys
from math import pow, sqrt


# 완전제곱수 판별 함수
def check_perfect_square_number(N):
    return sqrt(N).is_integer()


def make_number_coordinates():
    global N, M
    
    number_coordinates = []



    return number_coordinates

# 최대 완전제곱수 찾기
def get_max_psn():
    global arrA

    # 숫자 생성을 위한 x, y 좌표 확인
    # 선택되는 x와 y는 등차수열
    # 최대 자리수는 M > 이때는 x, y가 1씩 증가
        
    psn = []
    for x, y in make_number_coordinates():
        N = arrA[y][x]
        if check_perfect_square_number(N):
            psn.append(N)

    return psn

def main():
    
    result = get_max_psn()

    if len(result) == 0:
        return -1
    else:
        return max(result)


if __name__ == "__main__":
    input = sys.stdin.readline

    # (N x M)의 배열 A 생성
    N, M = map(int, input().strip().split())
    arrA = []
    for _ in range(N):
        arrA.append(list(input().strip()))

    # main 함수
    main()