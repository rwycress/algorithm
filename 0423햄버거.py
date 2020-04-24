def perm(k, n):
    global ans
    if k == n:
        if sum(cal) <= L:
            ans = max(sum(taste), ans)
    else:
        cal.append(data[k][1])
        taste.append(data[k][0])
        perm(k+1, n)
        cal.pop()
        taste.pop()
        perm(k+1, n)


import sys
sys.stdin = open("0423햄버거.txt", "r")
T = int(input())
for tc in range(T):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    cal = list()
    taste = list()

    perm(0, N)
    print("#{} {}".format(tc+1, ans))