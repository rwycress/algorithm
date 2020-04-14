import sys
sys.stdin = open("0319stylish.txt", "r")
T = int(input())
for tc in range(T):
    P, Q = map(int, input().split())
    data1 = [input() for _ in range(P)]
    data2 = [input() for _ in range(Q)]

    # 각 줄에서
    # a = '(' 누적
    # b = ')' 누적
    # c = '{' 누적
    # d = '}' 누적
    # e = '[' 누적
    # f = ']' 누적
    # 해당 줄을 들여쓰기 해야하는 칸 수: R(a-b) + C(c-d) + S(e-f)

    abcdef = [(0, 0, 0, 0, 0, 0)]*P
    ind = [0]*P

    a = b = c = d = e = f = 0
    for i in range(P):
        for j in range(len(data1[i])):
            if data1[i][j] == '(':
                a += 1
            elif data1[i][j] == ')':
                b += 1
            elif data1[i][j] == '{':
                c += 1
            elif data1[i][j] == '}':
                d += 1
            elif data1[i][j] == '[':
                e += 1
            elif data1[i][j] == ']':
                f += 1
        abcdef[i] = (a, b, c, d, e, f)

    for i in range(P):
        indent = 0
        # j == 0일 때:
        if data1[i][0] == '.':
            indent = 1
        # j >= 1일 때:
        for j in range(1, len(data1[i])):
            if data1[i][j - 1] == '.' and data1[i][j] == '.':
                indent += 1
        ind[i] = indent

    # 두 번째 줄의 indent와 첫 번째 줄의 a, b, c, d, e, f 값에서 R, C, S 값 추정
    rcs = []
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                flag = 0
                for i in range(1, P):
                    if R*(abcdef[i-1][0]-abcdef[i-1][1]) + C*(abcdef[i-1][2]-abcdef[i-1][3]) + S*(abcdef[i-1][4]-abcdef[i-1][5]) == ind[i]:
                        flag = 1
                    else:
                        flag = -1
                        break
                if flag == 1:
                    rcs.append((R, C, S))

    res = 0
    a1 = b1 = c1 = d1 = e1 = f1 = 0
    answer = '0 '

    for i in range(Q):
        for j in range(len(data2[i])):
            if data2[i][j] == '(':
                a1 += 1
            elif data2[i][j] == ')':
                b1 += 1
            elif data2[i][j] == '{':
                c1 += 1
            elif data2[i][j] == '}':
                d1 += 1
            elif data2[i][j] == '[':
                e1 += 1
            elif data2[i][j] == ']':
                f1 += 1

        indent1 = []
        for x in range(len(rcs)):
            if (rcs[x][0]*(a1-b1) + rcs[x][1]*(c1-d1) + rcs[x][2]*(e1-f1)) not in indent1:
                indent1.append(rcs[x][0]*(a1-b1) + rcs[x][1]*(c1-d1) + rcs[x][2]*(e1-f1))

        if len(indent1) == 1:
            res = indent1[0]
        else:
            res = -1

        if i < Q-1:
            answer += str(res) + ' '

    print("#{} {}".format(tc+1, answer[:-1]))



    indenp = [0]*p          #들여쓰기 온점 개수 기록
    codep = []
    codeq = []
    for i in range(P):
        codep.append(input())
    for i in range(Q):
        codeq.append(input())
    af = []
    A_F(codep, p)

    for i in range(P):
        cnt = 0
        while codep[i][cnt] == '.':
            cnt += 1
        indenp[i] = cnt

    rcs = RCS(af, indenp, p)

    af = []         #라인별 괄호 개수
    A_F(codeq, q)
    indenq = [0]*q
    for i in range(1, q):
        ab, cd, ef = af[i-1]        #이전 줄 까지의 괄호 수

    if rcs:
        R, C, S = rcs[0]
        ans = R*ab + C*cd + S*ef

        for x in rcs[1:]:
            R, C, S = x
            if R*ab + C*cd + S*ef != ans:
                indenq[i] = -1
                break
        if indenq[i] != -1:
            indenq[i] = ans



df A_F(code, I)""
    global af
    ab = 0
    cd = 0
    ef = 0
    for i in range(0, I):
        for j in range(len(code[i])):
            if code[i][j] == '(':
                ab += 1
            elif code[i][j] == ')':
                ab -= 1
            elif code[i][j] == '{':
                cd += 1
            elif code[i][j] == '}':
                cd -= 1
            elif code[i][j] == '[':
                ef += 1
            elif code[i][j] == ']':
                ef -= 1
        af.append((ab, cd, ef))


def RCS(af, indenp, p):
    org = []
    ab, cd, ef = af[0]
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                if p == 1:          #사용자 코드가 1줄일 때: 모든 R, C, S값이 후보가 됨
                    org.append((R, C, S))
                elif R*ab + C*cd + S*ef == indenp[1]:
                    org.append((R, C, S))

    for i in range(2, p):
        ab, cd, ef = af[i-1]
        dest = []
        for R, C, S in org:
            if R*ab + C*cd + S*ef == indenp[i]
                dest.append((R, C, S))
        org = dest

    return org
