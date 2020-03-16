import sys
sys.stdin = open("0309농자물수확.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    s = e = N // 2
    ans = 0
    for row in range(N):
        for i in range(s, e+1):
            ans += data[row][i]

        if row < N // 2:
            s, e = s - 1, e + 1
        else:
            s, e = s + 1, e - 1

    print(ans)