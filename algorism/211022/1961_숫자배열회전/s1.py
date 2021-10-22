import sys
sys.stdin = open('input.txt')

def turn90(arr):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = arr[N-1-j][i]
    return result


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(str,input().split())) for _ in range(N)]
    # print(arr)
    result1 = turn90(arr)
    result2 = turn90(result1)
    result3 = turn90(result2)

    # print(result1,result2,result3)
    print('#{}'.format(testcase))
    for i in range(N):
        print('{} {} {}'.format(''.join(result1[i]),''.join(result2[i]),''.join(result3[i])))