


for test in range(1, 11):
    test = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    max_num = 0
    for i in range(100):
        a = 0
        b = 0
        c = 0
        d = 0
        for j in range(100):
            a += board[i][j] # 가로
            b += board[j][i] # 세로
        c += board[i][i]
        d += board[i][99 - i]
        temp_max = max(a, b, c, d)
        if max_num < temp_max:
            max_num = temp_max


    print('#{} {}'.format(test, max_num))