import sys

sys.stdin = open('input1.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(arr, r, c, cnt):  # arr: 장기판, r:행, c:열, cnt : 움직인 횟수
    visited = [[0]*N  for _ in range(N)]
    stack = []

    stack.append((arr,r,c,cnt))
    while stack:
        current = stack.pop()
        carr = current[0]
        cr = current[1]
        cc = current[2]
        visited[cr][cc] += 1

        if current[3] >=3:
            continue
        for i in range(4):  # 현재 위치에서 상 우 하 좌 순으로 첫 적위치 탐색
            for j in range(1, N):
                ner = cr + dr[i] * j  # ner : next enemy row 상하좌우 탐색중 첫 적이있는 위치 그 적을 뛰어넘어야하므로..
                nec = cc + dc[i] * j  # nec : next enemy col 상하좌우 탐색중 첫 적이있는 위치 그 적을 뛰어넘어야하므로..
                if 0 <= ner < N and 0 <= nec < N and carr[ner][nec] == 1:
                    for k in range(1, N - 1):
                        nr = ner + k*dr[i]    # next row 로 갈수있는 위치
                        nc = nec + k*dc[i]    # next col 로 갈수있는 위치
                        if 0 <= nr < N and 0 <= nc < N:
                            if carr[nr][nc] == 1:  # 두번째 적이 나타났을때
                                carr[cr][cc] = 0
                                carr[nr][nc] = 2
                                stack.append((carr,nr,nc,current[3]+1))
                                carr[cr][cc] = 2
                                carr[nr][nc] = 1
                                break
                            else: # 두번째 적이 아직 안나타났을때
                                carr[cr][cc] = 0
                                carr[nr][nc] = 2
                                stack.append((carr, nr, nc, current[3] + 1))
                                carr[cr][cc] = 2
                                carr[nr][nc] = 0
    return visited


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    arr2 = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                arr2.append((i,j))
            if arr[i][j] == 2:
                r, c = i, j
    result = dfs(arr,r,c,0)
    cnt = 0
    for i,j in arr2:
        if result[i][j]>0:
            cnt += 1

    print(arr2)
    print('#{} {}'.format(testcase,cnt))

