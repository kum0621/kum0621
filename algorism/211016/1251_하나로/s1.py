import sys
sys.stdin = open('input.txt')   # round를 적용하는 시점을 맨마지막에 적용...

def prim(graph, s): # graph : 인접행렬, s: 시작정점
    key = [float('inf')] * N
    visited = [0] * N
    key[s] = 0

    for _ in range(N):
        minindex = -1
        min_val = float('inf')
        for i in range(N):
            if not visited[i] and key[i] < min_val:
                min_val = key[i]
                minindex = i
        visited[minindex] = 1
        for v in range(N):
            if not visited[v] and edge_cost[minindex][v] < key[v]:
                key[v] = edge_cost[minindex][v]
    return sum(key)

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    E = float(input())
    #print(arr)
    vertex = []
    for i in range(N):
        vertex.append((arr[0][i], arr[1][i]))
    #print(vertex)
    edge_cost = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            edge_cost[i][j] = (((vertex[i][0] - vertex[j][0])**2 + (vertex[i][1] - vertex[j][1])**2)*E)
    #print(edge_cost)
    print('#{} {}'.format(testcase, round(prim(edge_cost, 0))))

