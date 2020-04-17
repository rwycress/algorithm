# def game(n):
#     global win
#     if len(n) == 1:
#         return win
#     else:
#         win *= -1
#         a = n[-1] + n[-2]
#         if a < 10:
#             n.pop(-1)
#             n.pop(-1)
#             n.append(a)
#         elif a >= 10:
#             n.pop(-1)
#             n.pop(-1)
#             n.append(a // 10)
#             n.append(a % 10)
#         game(n)


def game2(n):
    global win
    cnt = 0
    total = sum(n)
    while total >= 10:
        total -= 9
        cnt += 1
    return cnt


import sys
sys.stdin = open("0417덧셈게임.txt", "r")
T = int(input())
for tc in range(T):
    data = str(input())

    num = [int(x) for x in data]
    win = -1                # 1: 앨리스, -1: 토끼

    plays = len(num) - 1 + game2(num)
    winner = win**(plays+1)

    if winner == -1:
        ans = "B"
    else:
        ans = "A"

    print("#{} {}".format(tc+1, ans))