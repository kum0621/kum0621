import sys
sys.stdin = open('sample_input.txt') # 유튭 강의 내용 크루스칼

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x
def union(x,y):
    p[find_set(y)] = find_set(x)

T = int(input())

for testcase in range(1,T+1):
    V, E = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])

    p = list(range(V+1))

    cnt = 0 # 간선을 선택한 횟수
    ans = 0 # 가중치를 더한값
    idx = 0 # edges 인덱스
    while cnt < V:
        n1 = edges[idx][0]
        n2 = edges[idx][1]

        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            ans += edges[idx][2]
        idx += 1
    print('#{} {}'.format(testcase, ans))