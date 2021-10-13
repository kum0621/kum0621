import sys
sys.stdin = open('sample_input.txt')
 # 뭐가 문제인지..
def course(i, length): # i :시작 vertex, length : vertex 개수
    global max_length
    if length > max_length: # 최대 길이 값 보다 길면 갱신
        max_length = length

    for j in range(len(edge_info)):
        if i in edge_info[j]:
            for k in range(2):
                if edge_info[j][k] != i:
                    next_vertex = edge_info[j][k]
            if visited[j] == 0:  # 방문하지 않은 곳
                visited[j] = 1   # 방문처리
                course(next_vertex, length+1)  # 다음 vertex 로 이동
                visited[j] = 0

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    edge_info = [list(map(int, input().split())) for _ in range(M)]  # 간선 정보
    vertex = [i for i in range(1, N+1)]   # 정점 정보
    max_length = 0

    for i in vertex:
        visited = [0] * (N + 1)
        visited[i] = 1
        course(i, 1)
    print('#{} {}'.format(testcase, max_length))
    #print(vertex)


