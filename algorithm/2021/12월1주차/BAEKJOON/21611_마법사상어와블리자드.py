# 첫째 줄에 N, M이 주어진다. 둘째 줄부터 N개의 줄에는 격자에 들어있는 구슬의 정보가 주어진다. r번째 행의 c번째 정수는 (r, c)에 들어있는 구슬의 번호를 의미한다.
# 어떤 칸에 구슬이 없으면 0이 주어진다. 상어가 있는 칸도 항상 0이 주어진다.
#
# 다음 M개의 줄에는 블리자드 마법의 방향 di와 거리 si가 한 줄에 하나씩 마법을 시전한 순서대로 주어진다.

#첫째 줄에 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)를 출력한다.

# 3 ≤ N ≤ 49
# N은 홀수
# 1 ≤ M ≤ 100
# 1 ≤ di ≤ 4
# 1 ≤ si ≤ (N-1)/2
# 칸에 들어있는 구슬이 K개라
# 상 하 좌 우 1, 2, 3, 4
def magic1(method):
    global SHARK_X, SHARK_Y
    direction, power = method[0], method[1]
    if direction == 1:
        for y in range(SHARK_Y - 1, SHARK_Y - power - 1, -1):
            MAP[y][SHARK_X] = 0
    elif direction == 2:
        for y in range(SHARK_Y + 1, SHARK_Y + power + 1):
            MAP[y][SHARK_X] = 0
    elif direction == 3:
        for x in range(SHARK_X - 1, SHARK_X - power - 1, -1):
            MAP[SHARK_Y][x] = 0
    else:
        for x in range(SHARK_X + 1, SHARK_X + power + 1):
            MAP[SHARK_Y][x] = 0

def magic2():
    global SHARK_X, SHARK_Y, N
    length = 1
    cnt = 0
    now_x = SHARK_X
    now_y = SHARK_Y
    lst = []
    # 1 : 상 , 2 : 하, 3 : 좌, 4: 우
    direction = 3
    while now_x != 0 or now_y != 0:
        # 상
        if direction == 1:
            if cnt == 2:
                length += 1
                cnt = 0
            for i in range(length):
                now_y -= 1
                if MAP[now_y][now_x] == 0:
                    continue
                lst.append(MAP[now_y][now_x])
            direction = 3
            cnt += 1

        # 하
        elif direction == 2:
            if cnt == 2:
                length += 1
                cnt = 0
            for i in range(length):
                now_y += 1
                if MAP[now_y][now_x] == 0:
                    continue
                lst.append(MAP[now_y][now_x])
            direction = 4
            cnt += 1

        # 좌
        elif direction == 3:
            if length == N - 1:
                for i in range(length):
                    now_x -= 1
                    if MAP[now_y][now_x] == 0:
                        continue
                    lst.append(MAP[now_y][now_x])
                break
            if cnt == 2:
                length += 1
                cnt = 0
            for i in range(length):
                now_x -= 1
                if MAP[now_y][now_x] == 0:
                    continue
                lst.append(MAP[now_y][now_x])
            direction = 2
            cnt += 1

        # 우
        else:
            if cnt == 2:
                length += 1
                cnt = 0
            for i in range(length):
                now_x += 1
                if MAP[now_y][now_x] == 0:
                    continue
                lst.append(MAP[now_y][now_x])
            direction = 1
            cnt += 1

    return lst

def magic3(lst):
    return_lst = lst

    stack = []

    explosion = True
    while explosion:
        temp_lst = []
        explosion = False
        for i in range(len(return_lst)):
            if len(stack) > 0:
                if stack[-1] != return_lst[i]:
                    if len(stack) >= 4:
                        SCORE[str(stack[-1])] += len(stack)
                        stack = [return_lst[i]]
                        explosion = True
                    else:
                        temp_lst.extend(stack)
                        stack = [return_lst[i]]

                elif stack[-1] == return_lst[i]:
                    stack.append(return_lst[i])
            else:
                stack.append(return_lst[i])

            if i == len(return_lst) - 1 and len(stack) >= 4:
                SCORE[str(stack[-1])] += len(stack)
                stack = []

        if stack:
            temp_lst.extend(stack)
            stack = []

        return_lst = temp_lst

    return return_lst

def magic4(lst):
    stack = []
    return_lst = []
    cnt = 1
    for i in range(len(lst)):
        if len(stack) > 0:
            if stack[-1] != lst[i]:
                return_lst.extend([cnt, stack[-1]])
                cnt = 1
                stack = [lst[i]]

            else:
                cnt += 1
        else:
            stack.append(lst[i])

    if stack:

        return_lst.extend([cnt, stack[-1]])

    if len(return_lst) + 1 < N * N:
        return_lst.extend([0 for _ in range(N * N - len(return_lst) + 1)])

    return return_lst

def magic5(lst):
    global SHARK_X, SHARK_Y, N
    temp_MAP = [[0 for i in range(N)] for j in range(N)]
    length = 1
    cnt = 0
    idx = 0
    now_x = SHARK_X
    now_y = SHARK_Y
    direction = 3
    # 상 : 1 하 : 2 좌 : 3 우 :4
    while idx < len(lst) and 0 <= now_x < N and 0<= now_y < N:
        if direction == 1:
            if cnt == 2:
                length += 1
                cnt = 0
            for i in range(length):

                now_y -= 1
                if idx >= len(lst) or 0 > now_x or now_x >= N or 0 > now_y or now_y >= N:
                    break
                MAP[now_y][now_x] = lst[idx]
                idx += 1
            direction = 3
            cnt += 1
        elif direction == 2:
            if cnt == 2:
                length += 1
                cnt = 0
            for i in range(length):
                now_y += 1
                if idx >= len(lst) or 0 > now_x or now_x >= N or 0 > now_y or now_y >= N:
                    break
                MAP[now_y][now_x] = lst[idx]
                idx += 1
            direction = 4
            cnt += 1
        elif direction == 3:
            if cnt == 2:
                length += 1
                cnt = 0
            for i in range(length):

                now_x -= 1
                if idx >= len(lst) or 0 > now_x or now_x >= N or 0 > now_y or now_y >= N:
                    break
                MAP[now_y][now_x] = lst[idx]
                idx += 1
            direction = 2
            cnt += 1
        else:
            if cnt == 2:
                length += 1
                cnt = 0
            for i in range(length):

                now_x += 1
                if idx >= len(lst) or 0 > now_x or now_x >= N or 0 > now_y or now_y >= N:
                    break
                MAP[now_y][now_x] = lst[idx]
                idx += 1
            direction = 1
            cnt += 1



N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
MAGIC = [list(map(int, input().split())) for _ in range(M)]
SHARK_X = N//2
SHARK_Y = N//2
SCORE = {'1' : 0, '2' : 0, '3' : 0}

for i in MAGIC:
    magic1(i)
    first_lst = magic2()
    second_lst = magic3(first_lst)
    third_lst = magic4(second_lst)
    magic5(third_lst)




print(SCORE['1'] + 2 * SCORE['2'] + 3 * SCORE['3'])
