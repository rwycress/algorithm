import sys
sys.stdin = open("0421통역사.txt", "r")
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     data = input()
#
#     upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower = 'abcdefghijklmnopqrstuvwxyz'
#     end = '.?!'
#
#     ans = ''
#     cnt = 0
#
#     word = ''
#     array = []
#
#     for d in data:
#         word += d
#         if d in end:
#             if word[0] == ' ':
#                 word = word[1:]
#             array.append(word)
#             word = ''
#
#     print(array)
#
#     for i in range(len(array)):
#         words = array[i].split()
#         #print(words)
#
#         flag = 0
#         cnt = 0
#         for w in words:
#             if len(w) > 2:
#                 for j in range(1, len(w)-1):
#                     if w[0] in upper:
#                         if w[j] in lower and w[-1] in lower:
#                             flag = 1
#                         elif w[j] in lower and w[-1] in end:
#                             flag = 1
#                         else:
#                             flag = 0
#                             break
#
#                     elif w[0] in lower:
#                         if w[j] in lower and w[-1] in end:
#                             flag = 1
#                         else:
#                             flag = 0
#
#             elif len(w) == 1 and w in upper:
#                 flag = 1
#
#             elif len(w) == 2 and w[-1] in end:
#                 if w[0] in lower or w[0] in upper:
#                     flag = 1
#
#             else:
#                 flag = 0
#
#             if flag == 1:
#                 cnt += 1
#             flag = 0
#         ans += str(cnt) + ' '
#
#     print("#{} {}".format(tc+1, ans[:-1]))


def chkname(li):
    global flag
    up = 0
    for i in li:
        if i.isalpha() and i == i.upper():
            up += 1
        elif i.isalpha() and i == i.lower():
            continue
        elif i == ' ':
            continue
        else:
            flag = False
            return flag
    if up == 1:
        flag = True
    else:
        flag = False
    return flag


T = int(input())
for tc in range(T):
    N = int(input())
    input_data = input()
    count = [0] * N
    end = '.!?'
    idx = 0
    stack = list()
    flag = True
    for i in input_data:
        if i == ' ' and len(stack):
            chkname(stack)
            if flag:
                count[idx] += 1
                stack = list()
            else:
                stack = list()
                flag = True
        elif i in end:
            chkname(stack)
            if flag:
                count[idx] += 1
                stack = list()
                idx += 1
            else:
                stack = list()
                idx += 1
                flag = True
        else:
            stack.append(i)
    print('#{}'.format(tc + 1), end=" ")
    for i in count:
        print(i, end=" ")
    print()