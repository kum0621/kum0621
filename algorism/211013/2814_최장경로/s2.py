import sys
sys.stdin = open('sample_input.txt')

def course(i, length): # i :시작 vertex, length : vertex 개수
    global max_length
    if length > max_length: # 최대 길이 값 보다 길면 갱신
        max_length = length

    for j in range(1,N+1):
        if graph[i][j] == 1 and not visited[j]:
            visited[j] = 1   # 방문처리
            course(j, length+1)  # 다음 vertex 로 이동
            visited[j] = 0

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    #edge_info = [list(map(int, input().split())) for _ in range(M)]  # 간선 정보

    graph = [[0]*(N+1) for _ in range(N+1)] # 2차원 행렬
    # vertex = [i for i in range(1, N+1)]   # 정점 정보
    for i in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    max_length = 0
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        visited[i] = 1
        course(i, 1)
        visited[i] = 0
    print('#{} {}'.format(testcase, max_length))
    #print(vertex)


