def AddToParent(arr):
    global L
    if visited.count(0) == 1:                      # 종료 조건(visited에서 0번 인덱스를 제외하고 모두 1일 때)
        return
    else:
        for i in range(len(arr)):
            if arr[i] and visited[i] == 0:         # 트리에서 값이 들어있는 노드를 찾아서 부모 노드에 더해줌
                arr[i//2] += arr[i]
                visited[i] = 1                     # 부모 노드로 값을 전달한 노드는 재귀 호출시 중복을 방지하기 위해 표시해둔다
        AddToParent(arr)                           # 반복


import sys
sys.stdin = open("0416노드의합.txt", "r")
T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(M)]

    tree = [0]*(N+1)                            # 트리
    visited = [0]*(N+1)                         # 부모에 값을 보내주는 과정이 끝난 노드를 표시하는 배열

    for i in range(len(data)):
        tree[data[i][0]] = data[i][1]           # 트리 초기화: 주어진 리프노드들부터 채우기

    AddToParent(tree)                           # 노드의 값을 부모노드에 합산하는 함수
    ans = tree[L]
    print("#{} {}".format(tc+1, ans))