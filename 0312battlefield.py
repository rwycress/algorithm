import sys
sys.stdin = open("0312battlefield.txt", "r")
T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    mapdata = [[x for x in input()] for _ in range(H)]
    N = int(input())
    inputdata = input()

    # 시작: 탱크 위치 찾기
    x = 0
    y = 0
    tank = '^v<>'
    for a in range(H):
        for b in range(W):
            if mapdata[a][b] in tank:
                x = a
                y = b
                break

    # 명령 입력
    for i in inputdata:
        if i == 'U':        #상
            if x > 0 and mapdata[x - 1][y] == '.':
                mapdata[x][y] = '.'
                mapdata[x - 1][y] = '^'
                x -= 1
            else:
                mapdata[x][y] = '^'
        elif i == 'D':      #하
            if x < (H - 1) and mapdata[x + 1][y] == '.':
                mapdata[x][y] = '.'
                mapdata[x + 1][y] = 'v'
                x += 1
            else:
                mapdata[x][y] = 'v'
        elif i == 'L':      #좌
            if y > 0 and mapdata[x][y - 1] == '.':
                mapdata[x][y] = '.'
                mapdata[x][y - 1] = '<'
                y -= 1
            else:
                mapdata[x][y] = '<'
        elif i == 'R':      #우
            if y < (W - 1) and mapdata[x][y + 1] == '.':
                mapdata[x][y] = '.'
                mapdata[x][y + 1] = '>'
                y += 1
            else:
                mapdata[x][y] = '>'
        elif i == 'S':      #격발:
            if mapdata[x][y] == '^':        #상향
                for s in range(1, x + 1):
                    if mapdata[x - s][y] == '*':
                        mapdata[x - s][y] = '.'
                        break
                    elif mapdata[x - s][y] == '#':
                        break
            elif mapdata[x][y] == 'v':      #하향
                for s in range(1, H - x):
                    if mapdata[x + s][y] == '*':
                        mapdata[x + s][y] = '.'
                        break
                    elif mapdata[x + s][y] == '#':
                        break
            elif mapdata[x][y] == '<':      #좌향
                for s in range(1, y + 1):
                    if mapdata[x][y - s] == '*':
                        mapdata[x][y - s] = '.'
                        break
                    elif mapdata[x][y - s] == '#':
                        break
            elif mapdata[x][y] == '>':      #우향
                for s in range(1, W - y):
                    if mapdata[x][y + s] == '*':
                        mapdata[x][y + s] = '.'
                        break
                    elif mapdata[x][y + s] == '#':
                        break

    # 결과 출력
    ans = ''
    for data in mapdata:
        for d in data:
            ans += d
        ans += '\n'
    ans = ans[:-1]

    print("#{} {}".format(tc+1, ans))