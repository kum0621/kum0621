import sys
sys.stdin = open('input1.txt')

import itertools

def exit_time(arr):
    arr = sorted(arr)
    current = 0
    for i in range(len(arr)):
        current = max(current, arr[i])
        current += 1
    return current



T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people = []
    exit = []
    distince = []
    exit_site= [0,1]
    min_time = 987654321
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people.append((i,j))
            elif arr[i][j] == 2:
                exit.append((i,j))
    #print(people,exit)

    for i in people:
        for j in range(2):
            if j == 0: # 첫번째 탈출구 까지 거리
                a = abs(i[0]-exit[j][0]) + abs(i[1]-exit[j][1])
            else:
                b = abs(i[0] - exit[j][0]) + abs(i[1] - exit[j][1])
        distince.append((a,b))
    exit_site = list(itertools.product(exit_site, repeat=len(distince)))

    for i in range(len(exit_site)):
        A = []
        B = []
        for j in range(len(distince)):
            if exit_site[i][j] == 0:
                A.append(distince[j][0])
            else:
                B.append(distince[j][1])
        #print(A)
        if max(exit_time(A),exit_time(B)) <min_time:
            min_time = max(exit_time(A),exit_time(B))
        #if max(exit_site(A), exit_site(B)) < min_time:
         #   min_time = max(exit_site(A), exit_site(B))

    print('#{} {}'.format(testcase,min_time))