import sys
sys.stdin = open("0316cutrod.txt", "r")
T = int(input())
for tc in range(T):
    data = input()

    rod = 0
    total = 0
    for i in range(len(data)):
        if data[i] == '(' and data[i+1] == ')':
            total += rod
            i += 1
        elif data[i-1] != '(' and data[i] == ')':
            rod -= 1
        elif data[i] == '(' and data[i+1] != ')':
            rod += 1
            total += 1

    print("#{} {}".format(tc+1, total))


    # 시간초과
    # for i in range(len(data)-1):
    #     if data[i]+data[i+1] == '()':
    #         data[i] = data[i+1] = '1'
    # data1 = ''.join(data)
    #
    # rodcuts = []
    # for i in range(len(data1)):
    #     if data1[i] == '(':
    #         rodn = 0
    #         for j in range(i+1, len(data1)):
    #             if data1[j] == '(':
    #                 rodn += 1
    #             elif data1[j] == ')':
    #                 rodn -= 1
    #                 if rodn == -1:
    #                     rodcuts.append(data1[i:j].count('1'))
    #                     break
    #
    # ans = 0
    # for r in rodcuts:
    #     ans += r//2 + 1
    # print("#{} {}".format(tc+1, ans))
