def func(level):
    if level == M : # 0 1 2 3 ... M-1
        for i in range(M):
            print(path[i], end = ' ')
        print()
        return

    for i in range(1, N + 1) : # 현재 선택할 수는 i
        if used[i] == 1 : continue
        used[i] = 1
        path[level] = i
        func(level + 1)
        path[level] = 0
        used[i] = 0



N,M = map(int ,input().split())
path = [0] * 8
used = [0] * 9 # 1 2 3 4 ... 8 index 를 이용해서 체크

func(0)