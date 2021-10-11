import sys
sys.stdin = open("sample_input.txt", "r")

def calculate(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    else:
        return num -10

def bfs():
    queue = [0] *100000
    front = -1
    rear = -1
    rear += 1
    queue[rear] = N
    visited[N] = 0

    while front != rear:
        front += 1
        curr_N = queue[front]
        if curr_N == M:
            return queue[M]
        for i in range(4):
            next_N = calculate(curr_N, i)
            if 0 < next_N <= 100000 and visited[next_N] == -1:
                visited[next_N] = visited[curr_N] + 1
                rear += 1
                queue[rear] = next_N

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [-1] * 100001

    print('#{} {}'.format(test_case, bfs()))