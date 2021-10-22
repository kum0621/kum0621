import sys
sys.stdin = open('input.txt')

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0
    start = N//2
    k = 0
    for i in range(N):
        if i < N//2:
            result -= arr[i][start]
            for j in range(k+1):
                result += arr[i][start+j]
                result += arr[i][start-j]
            k += 1
        else:
            result -= arr[i][start]
            for j in range(k+1):
                result += arr[i][start + j]
                result += arr[i][start - j]
            k -= 1


    print('#{} {}'.format(testcase, result))