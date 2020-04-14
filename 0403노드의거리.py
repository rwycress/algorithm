def bfs(x):
    global ans
    while que:
        x = que.pop(0)                                  # 출발 노드 설정
        for d in data:
            if x in d and visited[d[1]] == 0:           # 도착 노드가 뒷 자리에 표시된 경로 검색
                que.append(d[1])
                visited[d[1]] = visited[x] + 1
            elif x in d and visited[d[0]] == 0:         # 도착 노드가 앞 자리에 표시된 경로 검색
                que.append(d[0])
                visited[d[0]] = visited[x] + 1
            if x in d and G in d:                       # 목적지에 도착했을 경우 종료
                ans = visited[G] - 1
                break


import sys
sys.stdin = open("0403노드의거리.txt", "r")
T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    que = []
    visited = [0] * (V + 1)
    ans = 0                         # 기본값 = 0, 경로를 찾았을 경우 목적지까지의 거리로 바꿔줌

    # 초기화
    que.append(S)
    visited[S] = 1

    # 탐색
    bfs(S)

    print("#{} {}".format(tc+1, ans))