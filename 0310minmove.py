import sys
sys.stdin = open("0310minmove.txt", "r")
T = int(input())
for tc in range(T):
    W, H, N = map(int, input().split())
    x, y = map(int, input().split())
    ans = 0
    for _ in range(N-1):
        tx, ty = map(int, input().split())
        # 수직이동
        if x == tx:
            ans += abs(y - ty)
        # 수평이동
        elif y == ty:
            ans += abs(x - tx)
        # 좌상 <-> 우하
        elif (x < tx and y > ty) or (x > tx and y < ty):
            ans += abs(x - tx) + abs(y - ty)
        # 좌하 <-> 우상
        else:
            ans += max(abs(x - tx), abs(y - ty))

        x, y = tx, ty

    # 최단거리:
    # 1. 수직이동(x좌표 동일)
    # 2. 수평이동(y좌표 동일)
    # 3. 좌하 <-> 우상
    # (x1, y1) -> (x2, y2) 최단 거리는 max(x2-x1, y2-y1)이다

