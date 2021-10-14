import sys
from collections import deque
sys.stdin = open('sample_input.txt')

def dijkstra(s, graph): # graph: 인접행렬, s: 시작점    # 유튜브 라이브강의 및 두회님 코드도 참고..
    distances = [float('inf') for _ in range(N+1)]
    distances[s] = 0

    q = deque([0])
    # q = [0]
    while q:
        current = q.popleft()
        # current = q.pop(0)
        for next in range(N+1):
            if graph[current][next] and distances[current] + graph[current][next] < distances[next]:
                distances[next] = distances[current] + graph[current][next]
                if next != N:
                    q.append(next)
    return distances

T = int(input())
for testcase in range(1,T+1):
    N, E = map(int, input().split())
    #arr = [list(map(int, input().split())) for _ in range(E)]
    #print(arr)
    graph = [[0] *(N+1) for _ in range(N+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    print('#{} {}'.format(testcase, dijkstra(0, graph)[-1] ))
    #print(distances)
