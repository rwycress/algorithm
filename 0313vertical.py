import sys
sys.stdin = open("0313vertical.txt", "r")
T = int(input())
for tc in range(T):
    data = [[x for x in input()] for _ in range(5)]

    maxlen = 0
    for d in data:
        if len(d) > maxlen:
            maxlen = len(d)

    for i in range(5):
        while len(data[i]) < maxlen:
            data[i].append('')

    ans = ''
    for j in range(maxlen):
        for i in range(5):
            ans += data[i][j]

    print("#{} {}".format(tc+1, ans))