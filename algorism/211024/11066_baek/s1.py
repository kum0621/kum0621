import sys
sys.stdin = open('input.txt')

T= int(input())
for _ in range(1,T+1):
    n=int(input())
    num=list(map(int,input().split()))

    dp=list(list(0 for _ in range(n)) for _ in range(n))
    #if n=5
    for k in range(1,n):#k=1,2,3,4
        for i in range(n-k):#i=0,1,2,3,4 when k=1
            X,Y=i,i+k
            dp[X][Y]=2147000000
            for j in range(k):
                tmp=dp[X+1+j][Y]+dp[X][Y-k+j]
                dp[X][Y]=min(dp[X][Y],tmp)
            dp[X][Y]+=sum(num[X:Y+1])
    print(dp[0][-1])
