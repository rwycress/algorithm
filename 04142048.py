import sys
sys.stdin = open("04142048.txt", "r")
T = int(input())
for tc in range(T):
    N, S = input().split()
    N = int(N)
    data = [list(map(int, input().split())) for _ in range(N)]

    if S == 'left':
        for i in range(N):
            a = 0
            b = 0
            pos = 0
            for j in range(N):
                a = data[i][j]
                data[i][j] = 0
                if a != 0:
                    if b == 0:
                        b = a
                    elif b == a:
                        data[i][pos] = 2 * b
                        pos += 1
                        b = 0
                    elif b != a:
                        data[i][pos] = b
                        pos += 1
                        b = a
            if b != 0:
                data[i][pos] = b

    elif S == 'right':
        for i in range(N):
            a = 0
            b = 0
            pos = N-1
            for j in range(N-1, -1, -1):
                a = data[i][j]
                data[i][j] = 0
                if a != 0:
                    if b == 0:
                        b = a
                    elif b == a:
                        data[i][pos] = 2 * b
                        pos -= 1
                        b = 0
                    elif b != a:
                        data[i][pos] = b
                        pos -= 1
                        b = a
            if b != 0:
                data[i][pos] = b

    elif S == 'up':
        for j in range(N):
            a = 0
            b = 0
            pos = 0
            for i in range(N):
                a = data[i][j]
                data[i][j] = 0
                if a != 0:
                    if b == 0:
                        b = a
                    elif b == a:
                        data[pos][j] = 2 * b
                        pos += 1
                        b = 0
                    elif b != a:
                        data[pos][j] = b
                        pos += 1
                        b = a
            if b != 0:
                data[pos][j] = b

    elif S == 'down':
        for j in range(N):
            a = 0
            b = 0
            pos = N-1
            for i in range(N-1, -1, -1):
                a = data[i][j]
                data[i][j] = 0
                if a != 0:
                    if b == 0:
                        b = a
                    elif b == a:
                        data[pos][j] = 2 * b
                        pos -= 1
                        b = 0
                    elif b != a:
                        data[pos][j] = b
                        pos -= 1
                        b = a
            if b != 0:
                data[pos][j] = b

    print("#{}".format(tc+1))
    for i in range(N):
        ans = ' '.join(str(x) for x in data[i])
        print(ans)

    # ans = ''
    # for i in range(N):
    #     for d in data[i]:
    #         ans += str(d) + ' '
    #     ans += '\n'
    # print("#{}\n{}".format(tc+1, ans[:-1]))