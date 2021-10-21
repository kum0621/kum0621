import sys
sys.stdin = open('input1.txt')


dr = [-1,0,1,0]
dc = [0,1,0,-1]
def bfs(arr,r,c,cnt): # arr: 장기판, r:행, c:열, cnt : 움직인 횟수
    kill_possible = set()  # 죽일 수있는 말 위치 집합
    front = rear = -1
    rear += 1
    Q = [0]*10000000
    Q[rear] = (arr, r, c, cnt)

    while front != rear:
        front += 1
        current = Q[front]
        cr = current[1]
        cc = current[2]

        if current[3] < 3:
            for i in range(4):  # 현재 위치에서 상 우 하 좌 순으로 첫 적위치 탐색
                for j in range(1, N):
                    nr = cr + dr[i] * j
                    nc = cc + dc[i] * j
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                        for k in range(1,N-1):
                            if 0 <= nr+k*dr[i] < N and 0 <= nc+k*dc[i] < N:
                                x = 0
                                if arr[nr+k*dr[i]][nc+k*dc[i]] == 1:

                                    kill_possible.add((nr+k*dr[i], nc+k*dc[i]))
                                    #print(kill_possible)
                                    x = 1
                                arr[cr][cc] = 0
                                arr[nr+k*dr[i]][nc+k*dc[i]] = 2
                                rear += 1
                                Q[rear]= (arr, nr+k*dr[i], nc+k*dc[i], current[3]+1)
                                arr[cr][cc] = 2
                                arr[nr+k*dr[i]][nc+k*dc[i]] = x

    return kill_possible
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r,c = i,j
    # print(bfs(arr,r,c,0))

    print('#{} {}'.format(testcase,len(bfs(arr,r,c,0))))

