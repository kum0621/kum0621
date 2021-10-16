import sys
sys.stdin = open('input.txt')  #시간초과 ,, 9번 10번 케이스 오래걸림

from collections import deque

# def dijkstra(r, G):
#     D = [float('inf')]*N
#     P = [None]*N
#     visited = [False]*N
#     D[r] = 0
#
#     for _ in range(N):
#         min_index = -1
#         min_val = float('inf')
#         for i in range(N):
#             if not visited[i] and D[i] < min_val:
#                 min_val = D[i]
#                 min_index = i
#         visited[min_index] = True
#
#         for v, val in G[min_index]:
#             if not visited[v] and D[min_index] + val < D[v]:
#                 D[v] = D[min_index] + val
#                 P[v] = min_index
#     return D
def dijkstra(s, graph): # 시작점 s, 인접행렬: graph
    distances = [float('inf')] * (N + 1)
    distances[s] = 0
    Q = deque()
    Q.append(s)
    while Q:
        current = Q.popleft()
        for y, c in adj_mat[current]:
            if distances[current] + c < distances[y]:
                distances[y] = distances[current] + c
                Q.append(y)

    return distances


T = int(input())
for testcase in range(1,T+1):
    N, M, X = map(int, input().split())
    adj_mat = [[] for _ in range(N+1)]
    result = []
    for i in range(M):
        x, y, c = map(int, input().split())
        adj_mat[x].append((y, c))
    #print(adj_mat)
    go_home = dijkstra(X, adj_mat)
    for i in range(1,N+1):
        go_party = dijkstra(i, adj_mat)
        result.append(go_party[X]+go_home[i])
    print('#{} {}'.format(testcase, max(result)))


