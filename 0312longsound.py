import sys
sys.stdin = open("0312longsound.txt", "r")
T = int(input())
for tc in range(T):
    data = [x for x in input()]
    H = int(input())
    hy_data = list(map(int, input().split()))

    for a in range(len(hy_data)):
        hy_data[a] *= 2

    string = [''] * (2 * len(data) + 1)
    for i in range(1, len(string), 2):
        string[i] = data.pop(0)
    for hy in hy_data:
        string[hy] += '-'

    ans = str.join('', string)
    print("#{} {}".format(tc+1, ans))