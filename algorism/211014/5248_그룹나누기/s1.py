import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    person = [{i} for i in range(1, N+1)]
    # print(person)
    combi = list(map(int, input().split()))
    group_list = []
    for i in range(0, len(combi), 2):
        group = sorted([combi[i], combi[i+1]])
        group_list.append(group)
    # group_list.sort()
    # print(group_list)

    for i in range(len(group_list)):
        for j in range(N):
            if group_list[i][0] in person[j]:
                for k in range(N):
                    if group_list[i][1] in person[k]:
                        person[j] |= person[k]
                        if j != k:
                            person[k] = set()

                        # absorb = person.index(k)
                        # group_list.pop(absorb)
    # print(person)
    cnt = 0
    for i in person:
        if len(i) >= 1:
            cnt += 1
    print('#{} {}'.format(testcase, cnt))