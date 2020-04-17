def find(x):
    i = 1
    row = 1             # 행의 첫 번째 숫자
    while row <= x:
        row += i
        i += 1
    for j in range(0, i):
        if (row-i+1) + j == x:
            break
    return row-i+1, i-1, j+1        # (x가 위치한 열의 첫 번째 숫자, x가 위치한 열의 칸 수 = 높이, x가 위치한 열에서 x의 순서)

import sys
sys.stdin = open("0416피라미드.txt", "r")
T = int(input())
for tc in range(T):
    a, b = map(int, input().split())

    a_info = find(a)
    b_info = find(b)

    if a_info[0] < b_info[0]:               # a: 더 아래쪽에 위치함, b: 더 위쪽에 위치함
        a_info, b_info = b_info, a_info

    dx = 0
    dy = a_info[1] - b_info[1]

    if a_info[2] > b_info[2]:
        if a_info[2] - b_info[2] > dy:
            dx = a_info[2] - b_info[2] - dy
        else:
            dx = 0
    elif a_info[2] < b_info[2]:
        dx = abs(a_info[2] - b_info[2])

    ans = dx + dy
    print("#{} {}".format(tc+1, ans))
    print(dx, dy)