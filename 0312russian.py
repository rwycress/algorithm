import sys
sys.stdin = open("0312russian.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [[str(x) for x in input()] for _ in range(N)]

    case = []
    for w in range(1, N):
        for b in range(1, N):
            for r in range(1, N):
                if w + b + r == N:
                    case.append((w, b, r))

    anslist = []
    for c in case:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if i < c[0]:
                    if data[i][j] != 'W':
                        cnt += 1
                elif c[0] <= i < c[0] + c[1]:
                    if data[i][j] != 'B':
                        cnt += 1
                elif c[0] + c[1] <= i < c[0] + c[1] + c[2]:
                    if data[i][j] != 'R':
                        cnt += 1
        anslist.append(cnt)

    ans = min(anslist)
    print("#{} {}".format(tc+1, ans))