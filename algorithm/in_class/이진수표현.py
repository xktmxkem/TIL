T = int(input())

for tc in range(1, T+ 1):
    N,M = map(int, input().split())

    new_M = M & ((1 << N) -1)
    de = -1
    if (1 << N) - 1 == new_M :
        print("#{} ON".format(tc))
    else :
        print("#{} OFF".format(tc))