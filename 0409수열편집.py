import sys
sys.stdin = open("0409수열편집.txt", "r")
T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    list_data = list(map(int, input().split()))
    data = [list(map(str, input().split())) for _ in range(M)]

    for d in data:
        if d[0] == 'I':
            list_data.insert(int(d[1]), d[2])
        elif d[0] == 'D':
            list_data.pop(int(d[1]))
        elif d[0] == 'C':
            list_data[int(d[1])] = d[2]

    if L + 1 > len(list_data):
        ans = -1
    else:
        ans = list_data[L]

    print("#{} {}".format(tc+1, ans))