def count_node(p):
    global cnt
    cnt += 1
    if left[p]:
        count_node(left[p])
    if right[p]:
        count_node(right[p])


import sys
sys.stdin = open("0416subtree.txt", "r")
T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))

    parent = [0]*(E+2)
    left = [0]*(E+2)
    right = [0]*(E+2)
    cnt = 0

    for i in range(0, E*2, 2):
        if left[data[i]]:
            right[data[i]] = data[i+1]
        else:
            left[data[i]] = data[i+1]
        parent[data[i+1]] = data[i]

    count_node(N)
    print("#{} {}".format(tc+1, cnt))