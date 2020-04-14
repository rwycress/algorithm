import sys
sys.stdin = open("0402회전.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0

    while cnt < M:
        data.append(data.pop(0))
        cnt += 1

    print("#{} {}".format(tc+1, data[0]))