def f(n, a, b):
    global t
    if n == 7:
        num = 0
        for i in range(7):
            num = num*10 + number[i]
        t.add(num)
        return
    else:
        number[n] = data[a][b]
        for d in range(len(dy)):
            na = a + dy[d]
            nb = b + dx[d]
            if 0 <= na < N and 0 <= nb < N:
                f(n+1, na, nb)

import sys
sys.stdin = open("0305numbers.txt", "r")
T = int(input())
N = 4
for tc in range(T):
    data = [list(map(int, input().split())) for _ in range(N)]

    t = set()
    number = [0]*7
    dy = (0, 0, 1, -1)
    dx = (1, -1, 0, 0)
    for i in range(N):
        for j in range(N):
            f(0, i, j)

    print("#{} {}".format(tc+1, len(t)))