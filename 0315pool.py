def func(n, s):        # (n+1)월의 비용 계산할 것임, s: n월 까지의 비용 합
    global Min, d, m, q
    if n > 11:                  # 12월까지 계산이 끝난 다음에는 1년 이용권과 비교하고 끝냄
        if Min > s:
            Min = s
    elif Min <= s:              # 계산 중 비용합이 1년 이용권보다 비싸지는 경우에는 1년 이용권이 이득이므로 종료
        return
    else:
        func(n+1, s + min(d*data[(n+1)-1], m))       # 1개월 단위, 지금까지의 비용 합에 (n+1월 출석 수*1일 요금)과 (1개월 요금) 중 더 작은 값을 더함
        func(n+3, s + q)                             # 3개월 단위, 지금까지의 비용 합에 3개월 요금을 더함

import sys
sys.stdin = open("0315pool.txt", "r")
T = int(input())
for tc in range(T):
    d, m, q, y = map(int, input().split())
    data = list(map(int, input().split()))

    Min = y
    func(0, 0)

    print("#{} {}".format(tc+1, Min))



