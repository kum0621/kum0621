import sys
sys.stdin = open('input.txt')
from itertools import combinations
# def combi(arr):
#     result = []
#
#     while len(result) != N:
#

T = int(input())
for testcase in range(1,T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    S = sorted(S)
    result = []
    for i in range(1,N+1):
        for j in combinations(S, i):
            if sum(j) >= B:
                result.append(sum(j) - B)

    print('#{} {}'.format(testcase, min(result)))
    #while len(combi) != N: