import sys
sys.stdin = open("0310자기방.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())

    # 복도 배열을 새로 만들어놓고 학생이 지나갈때마다 경로에 1씩 더함
    # 모든 학생들이 이동한 후 복도 배열의 최대값이 겹치는 횟수 = 총 걸리는 시간

    cnt = [0]*201       # 복도: 1 ~ 200
    for _ in range(N):
        a, b = map(int, input().split())

        a = (a + 1) // 2
        b = (b + 1) // 2

        if a > b:
            a, b = b, a
        for i in range(a, b+1):
            cnt[i] += 1