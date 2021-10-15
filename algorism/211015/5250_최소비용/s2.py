#유튭 강의 내용

import sys
sys.stdin = open('sample_input.txt')

dr = [-1, 1, 0, 0] # 상하좌우
dc = [0, 0, -1, 1]

def BFS():
    Q = [0] * 1000000
    front = rear = -1

    rear += 1
    Q[rear] = (0,0)
    dist[0][0] = 0
    while front != rear:
        front += 1
        r, c = Q[front]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > arr[r][c]:
                    power = arr[nr][nc] -arr[r][c]
                else:
                    power = 0
                if dist[nr][nc] > dist[r][c] + power +1:
                    rear += 1
                    Q[rear] = (nr,nc)
                    dist[nr][nc] = dist[r][c] + power + 1


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]

    BFS()
    print('#{} {}'.format(testcase, dist[N-1][N-1]))