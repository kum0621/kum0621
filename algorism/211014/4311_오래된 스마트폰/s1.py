import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for testcase in range(1,T+1):
    N, O, M = map(int, input().split())  # N : 터치 가능한 숫자들의 개수 O : 터치 가능한 연산자들의 개수 , M : 최대 터치 가능한 횟수
    possible_num = list(map(int, input().split()))  # 가능한 숫자
    possible_oper = list(map(int, input().split()))  # 가능한 연산자 1 : + , 2 : -, 3 : *, 4 : /
    W = int(input())   # 원하는 숫자

    print(possible_num)
    print(possible_oper)
    print(W)
