def f(n, k, s):
    global maxV, u, w, data
    if n == k:
        if maxV < s*100:
            maxV = s*100
    elif maxV >= s*100:
        return
    else:
        for i in range(k):
            if u[i] == 0:
                u[i] = 1
                f(n+1, k, s*data[i][n]/100)
                u[i] = 0

import sys
sys.stdin = open("work.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    u = [0]*N
    w = [0]*N
    maxV = 0
    f(0, N, 1)

    print("#{} {:.6f}".format(tc+1, maxV))