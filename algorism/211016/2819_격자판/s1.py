import sys
sys.stdin = open('sample_input.txt')

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def make(num, i, j): #arr 격자판에서 i, j 7자리 숫자만들기
    num += arr[i][j]
    if len(num) == 7:
        result.add(num)
        return
    for k in range(4):
        if 0 <= i + dr[k] < 4 and 0 <= j + dc[k] < 4:
            nr = i + dr[k]
            nc = j + dc[k]
            make(num, nr, nc)

T = int(input())
for testcase in range(1,T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            num = ''
            result.add(make(num,i,j))
    print('#{} {}'.format(testcase, len(result)-1))
