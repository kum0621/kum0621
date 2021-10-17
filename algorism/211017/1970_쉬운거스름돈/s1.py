import sys
sys.stdin = open('input.txt')

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr =[0]*8
    while N>=10:
        if N >= 50000:
            arr[0] += 1
            N -= 50000
        elif N >= 10000:
            arr[1] += 1
            N -= 10000
        elif N >= 5000:
            arr[2] += 1
            N -= 5000
        elif N >= 1000:
            arr[3] += 1
            N -= 1000
        elif N >= 500:
            arr[4] += 1
            N -= 500
        elif N >= 100:
            arr[5] += 1
            N -= 100
        elif N >= 50:
            arr[6] += 1
            N -= 50
        else:
            arr[7] += 1
            N -= 10

    print('#{}'.format(testcase))
    for i in arr:
        print(i,end=" ")
    print()
    #print('{} {} {} {} {} {} {} {}'.format(won_50000,won_10000,won_5000,won_1000,won_500,won_100,won_50,won_10))
