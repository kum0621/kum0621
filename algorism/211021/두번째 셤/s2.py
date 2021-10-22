import sys
sys.stdin = open('input2.txt')

import copy

# def is_cycle(arr):
#     for i in range(len(arr)):
#         if arr[i][] >=
def work(arr):
    finish = [0]*(N+1)
    cnt = 0
    while arr != [0]*N:
        finish2 = copy.deepcopy(finish)
        for i in range(len(arr)):
            if arr[i] == 0:
                continue
            if len(arr[i]) == 2:
                if arr[i][1] == 0:
                    finish[i+1] = arr[i][0]
                    arr[i] = 0
                else:
                    if finish[arr[i][1]] != 0:
                        finish[i+1] = finish[arr[i][1]] + arr[i][0]
                        arr[i] = 0
            else:
                for j in range(1, len(arr[i])):
                    start_time = []
                    if finish[arr[i][j]] == 0:
                        break
                    else:
                        start_time.append(finish[arr[i][j]])
                else:
                    finish[i+1] = max(start_time) + arr[i][0]
                    arr[i] = 0
        else:
            if finish2 == finish:
                cnt += 1
            if cnt > 300:
                return -1
    return max(finish)

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr_list =[]


    for i in range(N):
        temp = copy.deepcopy(arr)
        temp[i][0] = temp[i][0]//2
        arr_list.append(temp)
    #print(arr_list)
    min_end = []
    for i in arr_list:
            min_end.append(work(i))
    print('#{} {}'.format(testcase, min(min_end)))
