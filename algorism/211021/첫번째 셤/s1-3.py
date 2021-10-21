import sys

sys.stdin = open('input1.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(arr, r, c, cnt,rst):  # arr: 장기판, r:행, c:열, cnt : 움직인 횟수
    global result
    if rst ==1:
        result.add((r,c))
    if cnt >=3:
        return

    for i in range(4):  # 현재 위치에서 상 우 하 좌 순으로 첫 적위치 탐색
        for j in range(1, N):
            if  0 <= r + dr[i] * (j-1) < N and 0 <= c + dc[i] * (j-1) < N:
                if arr[r + dr[i] * (j-1)][c + dc[i] * (j-1)] == 1:
                    break
            ner = r + dr[i] * j  # ner : next enemy row 상하좌우 탐색중 첫 적이있는 위치 그 적을 뛰어넘어야하므로..
            nec = c + dc[i] * j  # nec : next enemy col 상하좌우 탐색중 첫 적이있는 위치 그 적을 뛰어넘어야하므로..
            if 0 <= ner < N and 0 <= nec < N and arr[ner][nec] == 1:
                for k in range(1, N - 1):
                    nr = ner + k*dr[i]    # next row 로 갈수있는 위치
                    nc = nec + k*dc[i]    # next col 로 갈수있는 위치
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 1:  # 두번째 적이 나타났을때
                            arr[r][c] = 0
                            arr[nr][nc] = 2
                            dfs(arr,nr,nc, cnt+1,1)
                            arr[r][c] = 2
                            arr[nr][nc] = 1
                            break
                        else: # 두번째 적이 아직 안나타났을때
                            arr[r][c] = 0
                            arr[nr][nc] = 2
                            dfs(arr, nr, nc, cnt + 1,0)
                            arr[r][c] = 2
                            arr[nr][nc] = 0


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r, c = i, j
    result = set()

    dfs(arr,r,c,0,0)
    print(result)
    print('#{} {}'.format(testcase,len(result)))

