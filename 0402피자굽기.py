import sys
sys.stdin = open("0402피자굽기.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    que = [0]*N                     # 화덕에서 굽고있는 피자의 치즈 양
    pizza_in = [0]*N                # 화덕에서 굽고있는 피자의 번호
    idx = N                         # 피자 번호

    # 처음 피자를 화덕에 채운다
    for i in range(N):
        que[i] = data[i]
        pizza_in[i] = i+1

    # 피자굽기 시작
    cycle = 0
    while que.count(0) < N and idx < M:         # 모든 피자가 다 구워질때까지 계속 돌려보자
        if que[0] == 0:                         # 다 구워진 피자는 화덕의 1번 자리에 왔을 때 교체할 수 있다
            if idx <= M-1:
                que[0] = data[idx]
                pizza_in[0] = idx+1
                idx += 1
            else:                               # 다 구워진 피자를 계속 교체하다가 대기중인 피자가 없는 순간에 도달하면 잠시 멈추고 다음 단계로
                break
        que.append(que.pop(0))                  # 피자가 화덕안에서 잘 돌고 있다
        pizza_in.append(pizza_in.pop(0))
        cycle += 1
        if cycle % N == 0:                      # 한 바퀴를 돌 때마다 화덕안의 모든 피자의 치즈가 반이 녹는다
            for i in range(N):
                que[i] //= 2

    while que.count(0) < N:                     # 이제 화덕 안에 들어있는 피자만 다 굽히면 끝이므로 화덕안의 피자가 다 굽히는 순간까지만 돌려본다
        if que[0] == 0:
            pizza_in[0] = 'empty'               # 새로 넣어줄 피자가 더 이상 없으므로 피자없이 계속 돌고있는 자리는 따로 표시해둔다
        que.append(que.pop(0))
        pizza_in.append(pizza_in.pop(0))
        cycle += 1
        if cycle % N == 0:
            for i in range(N):
                que[i] //= 2

    ans = 0
    for i in range(N-1, -1, -1):                # 모든 피자가 다 굽힌 시점에서 화덕의 맨 뒷 번호(피자가 가장 늦게 나오는 자리)에 위치한 피자를 찾는다
        if pizza_in[i] != 'empty':
            ans = pizza_in[i]
            break

    print("#{} {}".format(tc+1, ans))