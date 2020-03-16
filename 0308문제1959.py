import sys
sys.stdin = open("1959.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        A, B = B, A
        N, M = M, N

    Max = -1000000
    for i in range(M - N + 1):
        S = 0
        for j in range(N):
            S += (A[j] * B[i + j])

        Max = max(Max, S)

    print("#{} {}".format(tc+1, Max))