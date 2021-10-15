import sys
sys.stdin = open('sample_input.txt')

dr = [-1, 1, 0, 0] # 상하좌우
dc = [0, 0, -1, 1]

def drive(r,c,fuel):
    global min_fuel

    if r == N-1 and c == N-1:
        if min_fuel > fuel:
            min_fuel = fuel
            return
        else:
            return
    if fuel > min_fuel:
        return

    stack = []
    #temp = []
    for i in range(4):
        if 0 <= r + dr[i] < N and 0 <= c + dc[i] < N and not visited[r + dr[i]][c + dc[i]]:

            if H[r + dr[i]][c + dc[i]] > H[r][c]:
                high = H[r + dr[i]][c + dc[i]] - H[r][c]
                stack.append((r + dr[i], c + dc[i], fuel+high+1))
            elif H[r + dr[i]][c + dc[i]] < H[r][c]:
                stack.append((r + dr[i], c + dc[i], fuel + 1))
            else:
                stack.append((r + dr[i], c + dc[i], fuel + 1))
    while stack:
        location = stack.pop()
        visited[location[0]][location[1]] = 1
        drive(location[0],location[1],location[2])
        visited[location[0]][location[1]] = 0



T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    min_fuel = float('inf')
    drive(0,0,0)
    print('#{} {}'.format(testcase, min_fuel))