import sys
sys.stdin = open("0310올림픽종목.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # i번째로 재밌는 종목
    # j번 위원
    # Ai: i종목을 개최하는데 드는 비용
    # Bj: 최대 가능 비용