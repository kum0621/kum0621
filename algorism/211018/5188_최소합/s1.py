import sys
sys.stdin = open('sample_input.txt')

dr = [1,0]
dc = [0,1]

def drive(r, c, c_sum):  # c_sum 현재 누적 합
    global min_sum
    if c_sum > min_sum:
        return
    if r == N-1 and c == N-1:
        if c_sum < min_sum:
            min_sum = c_sum
            return
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            drive(nr, nc, c_sum + arr[nr][nc])



T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    min_sum = N * N * 10
    drive(0,0,arr[0][0])
    print('#{} {}'.format(testcase,min_sum))
