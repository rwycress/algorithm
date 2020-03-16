import sys
sys.stdin = open("d1numbers.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    ops_num = list(map(int, input().split()))
    data = list(map(int, input().split()))

    # 연산자 나열
    ops = []
    for plus in range(ops_num[0]):
        ops.append('+')
    for minus in range(ops_num[1]):
        ops.append('-')
    for mul in range(ops_num[2]):
        ops.append('*')
    for div in range(ops_num[3]):
        ops.append('/')
    #print(ops)

    # 연산자 나열 가짓수
    def printAr(n):
        for i in range(n):
            ops_list.append(ops[l1[i]])
        ops_list2.append(ops_list)

    def perm(n, k):
        if k == n:
            printAr(n)
        else:
            for i in range(k, n):
                l1[k], l1[i] = l1[i], l1[k]
                perm(n, k + 1)
                l1[k], l1[i] = l1[i], l1[k]

    l1 = list(range(len(ops)))
    ops_list = []
    ops_list2 = []
    perm(len(ops), 0)

    # 수식 계산
    # res = data[0]
    # print(res)
    # for i in range(1, len(data)):
    #     if ops[0] == '+':
    #         res += data[i]
    #     elif ops[0] == '-':
    #         res -= data[i]
    #     elif ops[0] == '*':
    #         res *= data[i]
    #     elif ops[0] == '/':
    #         res /= data[i]
    #     ops = ops[1:]
    #     print(ops)
    #     print(res)
