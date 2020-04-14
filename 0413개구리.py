def chk_valid(arr):
    global ans
    if arr.count('c') == arr.count('r') == arr.count('o') == arr.count('a') == arr.count('k'):
        for i in range(len(arr)):
            if arr[i] == 'c':
                arr[i] = ''
                for j in range(i + 1, len(arr)):
                    if arr[j] == 'r':
                        arr[j] = ''
                        for k in range(j + 1, len(arr)):
                            if arr[k] == 'o':
                                arr[k] = ''
                                for l in range(k + 1, len(arr)):
                                    if arr[l] == 'a':
                                        arr[l] = ''
                                        for m in range(l + 1, len(arr)):
                                            if arr[m] == 'k':
                                                arr[m] = ''
                                                break
                                        break
                                break
                        break
    else:
        ans = -1

    for a in arr:
        if a != '':
            ans = -1
            break


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

    stack = []
    frogs = 0
    ans = 0

    string = ['0'] * len(data)
    for i in range(len(data)):
        string[i] = data[i]

    chk_valid(string)
    if ans == 0:
        cnt_frogs(data)
        ans = frogs

    print("#{} {}".format(tc+1, ans))
