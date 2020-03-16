import sys
sys.stdin = open("0310flies.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    anslist = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            kills = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    kills += data[k][l]
            anslist.append(kills)

    ans = max(anslist)
    print("#{} {}".format(tc+1, ans))