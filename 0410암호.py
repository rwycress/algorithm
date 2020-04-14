def func(cnt, idx):
    global startnum
    if cnt == K:
        return
    else:
        if idx < len(data):
            data.insert(idx, data[idx-1]+data[idx])
        elif idx > len(data):
            idx %= len(data)
            data.insert(idx, data[idx-1]+data[idx])
        elif idx == len(data):
            data.insert(idx, data[idx-1]+startnum)
        func(cnt+1, idx + M)


import sys
sys.stdin = open("0410암호.txt", "r")
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))

    startnum = data[0]
    func(0, M)

    ans = ''
    res = data[-1:-11:-1]
    for r in res:
        ans += str(r) + ' '

    print("#{} {}".format(tc+1, ans))