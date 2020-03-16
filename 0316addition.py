import sys
sys.stdin = open("0316addition.txt", "r")
T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    ans = A + B

    print("#{} {}".format(tc+1, ans))