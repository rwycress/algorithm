import sys
sys.stdin = open("0309단조증가.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    ans = -1
    flag = 0
    anslist = []
    for i in range(N):
        for j in range(i+1, N):
            number = data[i]*data[j]
            num = str(number)
            for a in range(0, len(num)-1):
                if num[a] <= num[a+1]:
                    flag = 0
                    continue
                else:
                    flag = 1
                    break
            if flag == 0:
                anslist.append(int(num))
    if anslist:
        ans = max(anslist)

    print("#{} {}".format(tc+1, ans))