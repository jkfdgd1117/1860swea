T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    ans = "Possible"
    bread = 0
    for time in range(max(customer)+1):
        # print(f'현재 {time}초')
        if time != 0 and time % M == 0:
            bread += K
        if time in customer:
            for _ in range(customer.count(time)):
                customer.remove(time)
                bread -= 1
                # print(f'제공 후 현재 빵 : {bread}')
                # print(f'제공 후 현재 예정 손님 : {customer}')
        if bread < 0:
            ans = "Impossible"
            break
        # print(f'현재 빵 : {bread}')
        # print(f'현재 예정 손님 : {customer}')
    print(f'#{test_case} {ans}')