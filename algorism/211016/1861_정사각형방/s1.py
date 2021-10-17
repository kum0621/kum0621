import sys
sys.stdin = open('input.txt')
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def course(i,j,cnt):

    Q = deque()
    Q.append((i,j,cnt))

    while Q:
        temp = Q.popleft()
        for k in range(4):
            nr = temp[0] + dr[k]
            nc = temp[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[temp[0]][temp[1]] + 1 == arr[nr][nc]:
                Q.append((nr,nc,temp[2]+1))
    return arr[i][j], temp[2]



T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    max_cnt = 0
    start = N ** 2 + 1
    for i in range(N):
        for j in range(N):
            s, cnt = course(i,j,1)
            #print(s,cnt)
            if cnt > max_cnt:
                max_cnt = cnt
                start = s
            elif cnt == max_cnt:
                if start > s:
                    start = s
    print('#{} {} {}'.format(testcase,start, max_cnt))