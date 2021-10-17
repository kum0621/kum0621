import sys
sys.stdin = open('sample_input.txt')

import copy

T = int(input())
for testcase in range(1,T+1):
    i2 = list(map(str, input()))
    i3 = list(map(str, input()))
    i2_list = []
    result = 0

    for i in range(len(i2)):
        temp = copy.deepcopy(i2)
        if i2[i] == '0':
            temp[i] = '1'
            temp = ''.join(temp)
            i2_list.append(int(temp, 2))
        else:
            temp[i] = '0'
            temp = ''.join(temp)
            i2_list.append(int(temp, 2))

    #print(i2_list)
    for i in range(len(i3)):
        temp = copy.deepcopy(i3)
        if i3[i] == '0':
            temp[i] = '1'
            temp1 = ''.join(temp)
            if int(temp1, 3) in i2_list:
                result = int(temp1, 3)
            temp[i] = '2'
            temp2 = ''.join(temp)
            if int(temp2, 3) in i2_list:
                result = int(temp2, 3)
        elif i3[i] == '1':
            temp[i] = '0'
            temp1 = ''.join(temp)
            if int(temp1, 3) in i2_list:
                result = int(temp1, 3)
            temp[i] = '2'
            temp2 = ''.join(temp)
            if int(temp2, 3) in i2_list:
                result = int(temp2, 3)
        else:
            temp[i] = '0'
            temp1 = ''.join(temp)
            if int(temp1, 3) in i2_list:
                result = int(temp1, 3)
            temp[i] = '1'
            temp2 = ''.join(temp)
            if int(temp2, 3) in i2_list:
                result = int(temp2, 3)
    print('#{} {}'.format(testcase, result))