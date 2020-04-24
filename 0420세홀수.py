def filter(num):
    for i in range(2, num):
        flag = 0
        for j in range(len(cand)):
            if i % cand[j] == 0:
                flag = 1
                break
        if flag == 0:
            cand.append(i)


import sys
sys.stdin = open("0420세홀수.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())

    cand = [2]
    ans = 0
    filter(N)

    for x in range(len(cand)):
        for y in range(x, len(cand)):
            for z in range(y, (len(cand))):
                if cand[x] + cand[y] + cand[z] == N:
                    ans += 1

    print("#{} {}".format(tc+1, ans))