import sys
sys.stdin = open('sample_input.txt')

def course(vrx): # vrx 에 사각형의 각 vertex 점좌표가 들어있는 리스트가 주어질 떄 tour로 가능하면 dessert 갯수 아니면 -1 return
    #dessert = [0]*101 # visited 개념으로 만듦 1부터 100까지의 디저트 수를 index와 맞추기 위해 index 0 은 그냥 만들었음
    dessert = []
    current_row = vrx[0][0] # 첫지점 행을 현재 행으로
    current_col = vrx[0][1] # 첫지점 열을 현재 열로
    #dessert[arr[current_row][current_col]] = 1
    dessert.append(arr[current_row][current_col])
    cnt = 1  # 디저트 갯수 카운트

    step = 1    # step1 : 시작점에서 왼쪽 아래 vertex까지 이동
                # step2 : 두번쨰 vertex까지 이동
                # step3 : 세번째 vertex까지 이동
                # step4 : 시작점까지 이동
#
    while step < 5: # 처음 위치로 되돌아오면 멈춤

        if step == 1:
            if current_row == vrx[1][0] and current_col == vrx[1][1]:
                step += 1
            else:

                current_row += 1
                current_col -= 1
                cnt += 1
                if arr[current_row][current_col] in dessert:  # 중복 디저트 검사
                    return -1
                else:
                    dessert.append(arr[current_row][current_col])
        elif step == 2:
            if current_row == vrx[2][0] and current_col == vrx[2][1]:
                step += 1
            else:

                current_row += 1
                current_col += 1
                cnt += 1
                if arr[current_row][current_col] in dessert:  # 중복 디저트 검사
                    return -1
                else:
                    dessert.append(arr[current_row][current_col])
        elif step == 3:
            if current_row == vrx[3][0] and current_col == vrx[3][1]:
                step += 1
            else:

                current_row -= 1
                current_col += 1
                cnt += 1
                if arr[current_row][current_col] in dessert:  # 중복 디저트 검사
                    return -1
                else:
                    dessert.append(arr[current_row][current_col])
        else:
            if current_row == vrx[0][0] and current_col == vrx[0][1]:
                cnt -= 1  # 도착지가 시작점이면 카운트 제외
                step += 1
                return cnt
            else:

                current_row -= 1
                current_col -= 1
                cnt += 1
                if arr[current_row][current_col] in dessert and current_row != vrx[0][0] :  # 중복 디저트 검사
                    return -1
                else:
                    dessert.append(arr[current_row][current_col])


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    result = []
    vertex = []  # 사각형의 꼭지점들이 추가되는곳
    # 시작점이후 아래로 반시계 방향으로 돌 때
    for i in range(0,N-2):   #시작점이 N-2, N-1 일때는 사각형 못만듦
        for j in range(1,N-1):  # 좌우 사이드에서는 왼쪽 , 오른쪽 대각선으로 못가므로 사각형 못만듦
            for k in range(1, N-1):  # 왼아래쪽 대각선으로 갈수있는 곳까지 가기
                if j-k < 0 or i+k > N-2: # 사각형 만들수 없는 범위 일때는 break
                    break
                else:  # 오른아래쪽 대각선으로 갈수있는곳까지 가기
                    for m in range(1, N-j): # 시작점에서 우측아래로 가능한 칸수
                        if i + k + m > N-1:  # 아래 한계점보다 넘어가는경우
                            break
                        else:
                            vertex.append([(i, j), (i+k, j-k), (i+k+m, j-k+m), (i+m,j+m)])

    for i in range(len(vertex)):
        result.append(course(vertex[i]))

    print('#{} {}'.format(testcase,max(result)))


