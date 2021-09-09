test = int(input())
for test in range(test):
    n, m = map(int, input().split())

    # 좌표평면 초기화
    fly_board = []
    for i in range(n):
        fly_board.append([0] * n)

    # 좌표평면 받아오기
    for i in range(n):
        fly_board[i] = list(map(int, input().split()))

    # 파리 수
    # 파리 수 리스트

    
    fly_ls = []


    move = 0

    for y in range(move, m):
        fly_cnt = 0
        for x in range(move, m):
            fly_cnt += fly_board[y][x]
        move += 1
        m += 1
        fly_ls.append(fly_cnt)
    
        print(fly_ls)
 