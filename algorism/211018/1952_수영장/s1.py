import sys
sys.stdin = open('sample_input.txt')

def ticket(cnt, price):
    global min_cost
    if min_cost < price:
        return
    if cnt > 11:
        if min_cost > price:
            min_cost = price
        return
    if plan[cnt] == 0:
        ticket(cnt+1,price)
        #return
    for i in range(3):
        if i == 0:
            nprice = plan[cnt] * cost[i] + price
            ticket(cnt + 1, nprice)
        elif i == 1:
            nprice = cost[i] + price
            ticket(cnt + 1, nprice)
        else:
            nprice = cost[i] + price
            ticket(cnt + 3, nprice)


T = int(input())
for testcase in range(1, T+1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_cost = cost[3]
    ticket(0,0)
    print('#{} {}'.format(testcase, min_cost))
