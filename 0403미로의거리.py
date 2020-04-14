def bfs(x, y):
    global ans
    while que:
        x, y = que.pop(0)
        for d in range(len(dx)):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 0 and visited[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            elif 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 3:             # 도착점 찾았을 때
                ans = visited[x][y] - 1
                break


import sys
sys.stdin = open("0403미로의거리.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [[int(x) for x in input()] for _ in range(N)]

    que = []
    visited = [[0]*N for _ in range(N)]
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    st = (0, 0)
    ans = 0                     # 답은 길을 못 찾을 때(0)를 기본값으로

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                st = (i, j)
                break

    # 초기화
    que.append(st)
    visited[st[0]][st[1]] = 1

    # 탐색
    bfs(st[0], st[1])

    print("#{} {}".format(tc+1, ans))