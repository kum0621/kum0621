import sys
sys.stdin = open('sample_input.txt')

def MST_PRIM(graph, s):  # graph : 인접행렬, s: 시작정점

    key = [float('inf')] * (V+1)  # 가중치를 무한대로 초기화
    pi = [0] * (V+1)              # 트리에 연결될 부모 정점 초기화
    visited = [0] * (V+1)         # 방문 표시 초기화
    key[s] = 0                    # 시작점 0 으로 가중치 설정

    for _ in range(V+1):  # 정점의 개수만큼 반복
        minindex = -1     #  -1 로 초기화
        min_val = float('inf')  # 무한대로 초기화
        for i in range(V+1):    # 방문안한 정점 중 최소 가중치 정점 찾기
            if not visited[i] and key[i] < min_val:
                min_val = key[i]
                minindex = i
        visited[minindex] = 1
        for v, w in graph[minindex]:
            if not visited[v] and w < key[v]:
                key[v] = w
                pi[v] = minindex
    return sum(key)

T = int(input())
for testcase in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((n2,w))
        graph[n2].append((n1,w))
    #print(graph)
    print('#{} {}'.format(testcase,MST_PRIM(graph,0)))