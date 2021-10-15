import sys
sys.stdin = open('input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def recovery():
    Q = [0]* 1000000
    front = rear = -1
    rear += 1
    Q[rear] = (0, 0)
    time[0][0] = 0
    while front != rear:
        front += 1
        r, c = Q[front]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if time[nr][nc] > time[r][c] + arr[nr][nc]:
                    rear += 1
                    Q[rear] = (nr, nc)
                    time[nr][nc] = time[r][c] + arr[nr][nc]

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    #arr = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
    arr = [list(map(int, input())) for _ in range(N)]
    time = [[float('inf')]*N for _ in range(N)]
    #print(arr)
    recovery()
    print('#{} {}'.format(testcase, time[-1][-1]))