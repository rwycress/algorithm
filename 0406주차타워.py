import sys
sys.stdin = open("0406주차타워.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())            # N: 주차 공간 수, M: 차량 수
    R = [int(input()) for _ in range(N)]        # R: 각 주차 공간의 단위 무게당 요금
    W = [int(input()) for _ in range(M)]        # W: 각 차량의 무게
    data = [int(input()) for _ in range(2*M)]   # 차량 진입 / 퇴장 순서

    parking = [0] * N
    toll = 0

    for i in range(2*M):
        if parking.count(0) > 0:
            if data[i] > 0:
                for j in range(N):
                    if parking[j] == 0:
                        parking[j] = data[i]
                        toll += R[j] * W[data[i]-1]
                        break
            elif data[i] < 0 and -data[i] in parking:
                for k in range(N):
                    if parking[k] == -data[i]:
                        parking[k] = 0
                        data[i] = 0
                        break

        elif parking.count(0) == 0:
            for j in range(i, 2*M):
                if data[j] < 0 and -data[j] in parking:
                    for k in range(N):
                        if parking[k] == -data[j]:
                            parking[k] = 0
                            data[j] = 0
                            break
                    break
            if data[i] > 0:
                for j in range(N):
                    if parking[j] == 0:
                        parking[j] = data[i]
                        toll += R[j] * W[data[i]-1]
                        break

    print("#{} {}".format(tc+1, toll))