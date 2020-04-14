def subset(k, n):
    if k == n:
        possible.append(list(A))
    else:
        A.append(data[k])
        subset(k + 1, n)
        A.pop()
        subset(k + 1, n)


import sys
sys.stdin = open("0407알파벳공부.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [input() for _ in range(N)]

    A = []
    possible = []

    subset(0, N)
    cnt = len(possible)

    for i in range(len(possible)):
        alphabets = [0] * (ord('z') + 1)
        for j in range(len(possible[i])):
            for l in range(len(possible[i][j])):
                alphabets[ord(possible[i][j][l])] += 1

        for x in range(ord('a'), ord('z')+1):
            if alphabets[x] == 0:
                cnt -= 1
                break

    print("#{} {}".format(tc+1, cnt))



