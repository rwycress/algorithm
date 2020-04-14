def dfs(x, y):
    global string
    for d in range(len(dx)):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            string += str(data[nx][ny])
        if string in str_list:
            continue



        if len(string) == 7 and string not in str_list:
            str_list.append(string)


        if 0 <= nx < 4 and 0 <= ny < 4 and len(string) == 7:


import sys
sys.setrecursionlimit(100000)
sys.stdin = open("0405격자판.txt", "r")
T = int(input())
for tc in range(T):
    data = [list(map(int, input().split())) for _ in range(4)]

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    string = ""
    str_list = []

    for i in range(4):
        for j in range(4):
            string += data[i][j]
            for k in range(7):


    print(len(str_list))
    print(str_list)