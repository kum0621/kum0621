
def Y_axis(arr,N):  # 좌우 대칭
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = arr[i][N-j-1]
    return result

def X_axis(arr,N): # 상하 대칭
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = arr[N-i-1][j]
    return result

def XY_axis(arr,N): # 대각선 대칭
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[N-j-1][N-i-1] = arr[i][j]
    return result

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 기본이 되는 판
    result = [[0]*(2*N) for _ in range(2*N)] # 결과를 담을 리스트

    for i in range(N):  # 출력양식에 맞게 출력 문자열로 받아야 join 쓸수있기 때문에 str로 받기
        for j in range(N):
            result[i][j] = str(arr[i][j])
            result[i][j+N] = str(Y_axis(arr,N)[i][j])
            result[i+N][j] = str(X_axis(arr, N)[i][j])
            result[i+N][j+N] = str(XY_axis(arr, N)[i][j])

    print('#{}'.format(testcase))
    for i in range(2*N):
        print(" ".join(result[i]))
