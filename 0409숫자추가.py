import sys
sys.stdin = open("0409숫자추가.txt", "r")
T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    list_data = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(M)]          # (추가할 인덱스, 추가할 숫자)

    for d in data:
        list_data.insert(d[0], d[1])

    print("#{} {}".format(tc+1, list_data[L]))