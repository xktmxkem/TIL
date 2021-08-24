T = int(input())
 
# 출력값 저장
res_list = ['O won', 'X won', 'Draw', 'Game has not completed']
 
# 출력에 필요한 index 값 저장
my_items = []
 
for tc in range(T):
 
    # 주어진 input이 T-1이 전에는 5줄임
    if tc < T - 1:
        board = [list(input()) for _ in range(5)]
 
    else:
        board = [list(input()) for _ in range(4)]
 
    # '.'이 없으면 0 있으면 1
    check = 0
 
    # 이긴 사람이 있으면 1 없으면 0
    res = 0
 
    # 행,열 확인
    for q in range(4):
        temp_row = 0
        temp_col = 0
        cnt_row = 0
        cnt_col = 0
        for w in range(4):
 
            # 행의 값이 변하지 않았으면
            if temp_row == 0:
 
                # 해당 index의 값이 X 나 O이면 cnt + 1 해주고, temp에 저장
                if board[q][w] == 'X' or board[q][w] == 'O':
                    cnt_row += 1
                    temp_row = board[q][w]
 
                # '.'이면 check 바꾸기
                elif board[q][w] == '.':
                    check = 1
 
                # T이면 cnt + 1 만
                else:
                    cnt_row += 1
 
            # 행의 값에 X or O가 저장된 상태면
            else:
 
                # 현재 index의 값이 temp에 저장된 값이랑 같거나 T이면
                if (board[q][w] == temp_row) or board[q][w] == 'T':
                    cnt_row += 1
 
                elif board[q][w] == '.':
                    check = 1
 
            if temp_col == 0:
                if board[w][q] == 'X' or board[w][q] == 'O':
                    cnt_col += 1
                    temp_col = board[w][q]
 
                elif board[w][q] == '.':
                    check = 1
 
                else:
                    cnt_col += 1
 
            else:
                if (board[w][q] == temp_col) or board[w][q] == 'T':
                    cnt_col += 1
 
                elif board[w][q] == '.':
                    check = 1
 
        # cnt가 4인 경우, 저장된 값에 따라 my_items에 저장
        if cnt_row == 4:
            if temp_row == 'O':
                my_items.append(0)
 
            else:
                my_items.append(1)
 
            # res값 변경
            res = 1
            break
 
        if cnt_col == 4:
            if temp_col == 'O':
                my_items.append(0)
 
            else:
                my_items.append(1)
 
            res = 1
            break
 
    # 대각선 확인
    if res == 0:
        temp_cross1 = 0
        temp_cross2 = 0
        cnt_cross1 = 0
        cnt_cross2 = 0
        for qq in range(4):
            if temp_cross1 == 0:
                if board[qq][qq] == 'O' or board[qq][qq] == 'X':
                    cnt_cross1 += 1
                    temp_cross1 = board[qq][qq]
 
                elif board[qq][qq] == 'T':
                    cnt_cross1 += 1
 
            else:
                if (board[qq][qq] == temp_cross1) or board[qq][qq] == 'T':
                    cnt_cross1 += 1
 
            if temp_cross2 == 0:
                if board[qq][3 - qq] == 'O' or board[qq][3 - qq] == 'X':
                    cnt_cross2 += 1
                    temp_cross2 = board[qq][3 - qq]
 
                elif board[qq][3 - qq] == 'T':
                    cnt_cross2 += 1
 
            else:
                if (board[qq][3 - qq] == temp_cross2) or board[qq][3 - qq] == 'T':
                    cnt_cross2 += 1
 
        if cnt_cross1 == 4:
            if temp_cross1 == 'O':
                my_items.append(0)
 
            else:
                my_items.append(1)
 
            res = 1
 
        if cnt_cross2 == 4:
            if temp_cross2 == 'O':
                my_items.append(0)
 
            else:
                my_items.append(1)
 
            res = 1
 
    if res == 0:
        
        # '.'이 없었으면
        if check == 0:
            
            # Draw
            my_items.append(2)
 
        else:
            
            # 그 외
            my_items.append(3)
 
idx = 1
for r in my_items:
    print('#{} {}'.format(idx, res_list[r]))
    idx += 1