import sys
from collections import deque
sys.stdin = open('sample_input.txt')
# def calculate(N, operator): # 0 : +!, 1: -1, 2: *2, 3: -10
#     if operator == 0:
#         return N+1
#     elif operator == 1:
#         return N-1
#     elif operator == 2:
#         return N*2
#     else:
#         return N-10

def bfs(): # 영상 참고
    Q = deque()
    Q.append(N)
    visited[N] = 1

    ans = 0
    while Q:
        for i in range(len(Q)):
            num = Q.popleft()
            if num == M:
                return ans

            for j in (num+1, num-1, num*2, num-10):
                if 0 < j <= 1000000 and not visited[j]:
                    visited[j] = 1
                    Q.append(j)
        ans += 1



T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    print('#{} {}'.format(testcase, bfs()))
