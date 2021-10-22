import sys
sys.stdin = open('input2.txt')

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    passenger = list(map(int, input().split()))
    result = []

    candid_AB = set()
    for i in range(N):
        for j in range(N):
            if (i+1) % N != j and (i-1) % N != j and i != j:
                for k in range(N):
                    for m in range(N):
                        if k != i and k != j and k != m and m != i and m != j and (k+1) % N != i and (k-1) % N != i and (k+1) % N != j and (k-1) % N != j and (m+1) % N != i and (m-1) % N != i and (m+1) % N != j and (m-1) % N != j and (k+1) % N != m and (k-1) % N != m:
                            if i < j and k < m:
                                if i < m < j and i < k < j:

                                    result.append((passenger[i]+passenger[j])**2 + (passenger[k]+passenger[m])**2)
                                elif i > m > k or j < k < m or k<i<j<m :

                                    result.append((passenger[i]+passenger[j])**2 + (passenger[k]+passenger[m])**2)


    print('#{} {}'.format(testcase, max(result)))