import sys
sys.stdin = open('input.txt')  #시간초과 ,, 9번 10번 케이스 오래걸림

from collections import deque

def dijkstra(s, graph): # 시작점 s, 인접행렬: graph
    distances = [float('inf')] * (N + 1)
    distances[s] = 0
    Q = deque()
    Q.append(s)
    while Q:
        current = Q.popleft()
        for n in range(N+1):
            if adj_mat[current][n] and distances[current] + adj_mat[current][n] < distances[n]:
                distances[n] = distances[current] + adj_mat[current][n]
                Q.append(n)

    return distances

T = int(input())
for testcase in range(1,T+1):
    N, M, X = map(int, input().split())
    adj_mat = [[0] * (N+1) for _ in range(N+1)]
    result = []
    for i in range(M):
        x, y, c = map(int, input().split())
        adj_mat[x][y] = c
    #print(adj_mat)
    go_home = dijkstra(X, adj_mat)
    for i in range(1,N+1):
        go_party = dijkstra(i, adj_mat)
        result.append(go_party[X]+go_home[i])
    print('#{} {}'.format(testcase, max(result)))


