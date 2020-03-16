import sys
sys.stdin = open("0310sudoku.txt", "r")
T = int(input())
for tc in range(T):
    N = 9
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 1
    # 행 검증
    for i in range(9):
        row = [0]*10    # 1 ~ 9의 개수를 나타낼 배열
        for j in range(9):
            if row[data[i][j]]:     # row[n]이 1이면 = n이 이미 있으면
                ans = 0
                break
            row[data[i][j]] = 1

    # 열 검증
    for j in range(9):
        col = [0] * 10
        for i in range(9):
            if col[data[i][j]]:
                ans = 0
                break
            col[data[i][j]] = 1

    # 3x3 사각 영역 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            rect = [0]*10
            # 왼쪽 모서리 (i, j)에서 높이 = 너비 = 3
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if rect[data[x][y]]:
                        ans = 0
                        break
                    rect[data[x][y]] = 1

    print("#{} {}".format(tc+1, ans))