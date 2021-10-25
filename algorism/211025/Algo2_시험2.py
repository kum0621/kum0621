
# 2단계 풀이
def sum_course(row, c_sum, visited):
    global min_sum
    if min_sum < c_sum: # 이미 최소합보다 커지면 리턴 (가지치기)
        return
    if row == N: # 마지막 행 일때까지 가지치기에서 걸러지지 않았다면 최소합 갱신
        min_sum = c_sum
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            nc_sum = c_sum + arr[row][i]
            sum_course(row+1,nc_sum, visited)
            visited[i] = 0

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_sum = 99999999999
    visited = [0] * N
    sum_course(0,0, visited)
    print('#{} {}'.format(testcase,min_sum))
