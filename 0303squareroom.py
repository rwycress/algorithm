def dfs(a, b):
    global cnt
    for d in range(len(i_dy)):
        ni = a + i_dy[d]
        nj = b + j_dx[d]
        if 0 <= ni < N and 0 <= nj < N and data[ni][nj] == data[a][b] + 1:
            cnt += 1
            dfs(ni, nj)

import sys
sys.setrecursionlimit(4000)
sys.stdin = open("squareroom.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    #print(data)

    i_dy = (1, -1, 0, 0)
    j_dx = (0, 0, 1, -1)
    maxcnt = 0
    ans = 0
    ans_list = []

    for i in range(N):
        for j in range(N):
            cnt = 1
            dfs(i, j)
            if cnt >= maxcnt:
                maxcnt = cnt
                ans_list.append((maxcnt, data[i][j]))
    #print(ans_list)

    ans_list2 = []
    for i in range(len(ans_list)):
        if ans_list[i][0] == ans_list[-1][0]:
            ans_list2.append(ans_list[i][1])

    ans = min(ans_list2)
    print("#{} {} {}".format(tc+1, ans, maxcnt))
