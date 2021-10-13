import sys
sys.stdin = open('sample_input.txt')
from itertools import combinations


def item_div(N): # 식재료 나누는 경우의 수 구하기
    item = [i for i in range(N)]
    combinate = list(combinations(item, N//2)) # 식재료 조합
    result = []
    for i in range(len(combinate)):
        arr = [0] * N
        for j in range(N//2):
            arr[combinate[i][j]] = 1
        result.append(arr)
    return result


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    different_AB = [] # 맛차이

    for i in item_div(N):
        A = 0
        B = 0
        for j in range(N):
            for k in range(N):
                if i[j] == 0 and i[k] == 0:
                    A += synergy[j][k]
                if i[j] == 1 and i[k] == 1:
                    B += synergy[j][k]
        different_AB.append(abs(A-B))
        #print(A,B)
    print('#{} {}'.format(testcase, min(different_AB)))