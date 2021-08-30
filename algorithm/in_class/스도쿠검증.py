


T = int(input())

for testcase in range(1, T + 1):
    board = [list(map(int, input().split())) for i in range(9)]

    ret = 1
    for y in range(9):
        check_garo = [i for i in range(1, 10)]
        check_sero = [i for i in range(1, 10)]
        check_cube = [i for i in range(1, 10)]
        for x in range(9):
            try:
                check_garo.remove(board[y][x])
                check_sero.remove(board[x][y])
                if (y == 0 and x == 0) or (y == 3 and x == 3) or (y == 6 and x == 6):
                    for i in range(3):
                        for j in range(3):
                            check_cube.remove(board[y + i][x + j])
            except:
                ret = 0
                break
        if ret == 0:
            break
    print('#{} {}'.format(testcase, ret))
