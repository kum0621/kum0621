import sys
sys.stdin = open('sample_input.txt')

from itertools import product

def col_permut(a,b): # 0부터 a-1 개의 숫자를 중복 가능하게 b번 뽑은 순열리스트
    arr = [i for i in range(a)]
    result = list(product(arr, repeat=b))
    return result

def target_row(arr):
    target_result = []
    for i in range(W):
        for j in range(H):
            if arr[j][i] != 0:
                target_result.append(j)
                break
    return target_result

def drop_col(arr, col):
    row = target_row(current_plate)
    influence_brick(arr, row, col)

def influence_brick(arr, row, col):
    brick_range = arr[row][col] - 1
    visited = [[0] * H for _ in range(W)]

    for i in range(brick_range):
        if row + i <= H - 1:
            if arr[row + i][col] > 0:
                b
        if row - i >= 0:
            arr[row - i][col] = 0
        if col + i <= W - 1:
            arr[row][col + i] = 0
        if col - i >= 0:
            arr[row][col - i] = 0

T = int(input())
for testcase in range(1, T + 1):
    N, W, H = map(int, input().split())
    plate = [list(map(int, input().split())) for _ in range(H)]

    print(col_permut(W, N))
    #print(zero_cnt)
    #print(target_row(plate))

    for i in col_permut(W, N): # 각 경우의 수 별로 벽돌 남은갯수 계산
        current_plate = plate
        for j in range(N):
            drop_col(current_plate,j)

            current_plate = next_plate

