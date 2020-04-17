def chk_valid(arr):
    global ans
    if arr.count('c') == arr.count('r') == arr.count('o') == arr.count('a') == arr.count('k'):
        # for i in range(len(arr)):
        #     if arr[i] == 'c':
        #         arr[i] = ''
        #         for j in range(i + 1, len(arr)):
        #             if arr[j] == 'r':
        #                 arr[j] = ''
        #                 for k in range(j + 1, len(arr)):
        #                     if arr[k] == 'o':
        #                         arr[k] = ''
        #                         for l in range(k + 1, len(arr)):
        #                             if arr[l] == 'a':
        #                                 arr[l] = ''
        #                                 for m in range(l + 1, len(arr)):
        #                                     if arr[m] == 'k':
        #                                         arr[m] = ''
        #                                         break
        #                                 break
        #                         break
        #                 break
        for i in range(len(arr)):
            if arr[i] == 'c':
                chk[0] += 1
            elif arr[i] == 'r':
                chk[1] += 1
            elif arr[i] == 'o':
                chk[2] += 1
            elif arr[i] == 'a':
                chk[3] += 1
            elif arr[i] == 'k':
                chk[4] += 1
            if chk[0] < chk[1] or chk[1] < chk[2] or chk[2] < chk[3] or chk[3] < chk[4]:
                ans = -1
                break
    else:
        ans = -1
    # for a in arr:
    #     if a != '':
    #         ans = -1
    #         break


def cnt_frogs(arr):
    global frogs
    for i in range(len(arr)):
        if arr[i] == 'c':
            stack.append(arr[i])
        elif arr[i] == 'k':
            stack.pop(-1)
        if frogs < len(stack):
            frogs = len(stack)


import sys
sys.stdin = open("0413개구리.txt", "r")
T = int(input())
for tc in range(T):
    data = [x for x in input()]

    chk = [0]*5
    stack = []
    frogs = 0
    ans = 0

    #string = data[:]

    chk_valid(data)
    if ans == 0:
        cnt_frogs(data)
        ans = frogs

    print("#{} {}".format(tc+1, ans))
