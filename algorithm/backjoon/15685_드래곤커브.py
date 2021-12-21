# 즉, K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것이다.
#
# 크기가 100×100인 격자 위에 드래곤 커브가 N개 있다. 이때, 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하는 프로그램을 작성하시오. 격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표이다.
#
# 입력
# 첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 드래곤 커브의 정보가 주어진다.
# 드래곤 커브의 정보는 네 정수 x, y, d, g로 이루어져 있다.
# x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
#
# 입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.
#
# 방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.
#
# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
# 출력
# 첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.
import heapq
def plus_route(stack):
    return_lst = stack

    for i in range(len(stack) -1, -1, -1):
        if stack[i] == 0:
            return_lst.append(1)
        elif stack[i] == 1:
            return_lst.append(2)
        elif stack[i] == 2:
            return_lst.append(3)
        elif stack[i] == 3:
            return_lst.append(0)

    return return_lst

def curve(x, y, d, g):
    stack = [d]
    MAP[y][x] = 1
    ny = y
    nx = x
    n_idx = 0

    for i in range(g + 1):
        for j in range(n_idx, len(stack)):
            if stack[j] == 0:
                MAP[ny][nx + 1] = 1
                nx += 1
            elif stack[j] == 1:
                MAP[ny - 1][nx] = 1
                ny -= 1
            elif stack[j] == 2:
                MAP[ny][nx - 1] = 1
                nx -= 1
            elif stack[j] == 3:
                MAP[ny + 1][nx] = 1
                ny += 1
        stack = plus_route(stack)
        n_idx = len(stack) // 2




N = int(input())
MAP = [[0 for i in range(101)] for j in range(101)]
for i in range(N):
    x, y, d, g = map(int, input().split())
    curve(x, y, d, g)

rec_count = 0
for y in range(101):
    for x in range(101):
        if MAP[y][x] == 1:
            if y + 1 < len(MAP) and x + 1 < len(MAP):
                if MAP[y][x + 1] == 1 and MAP[y + 1][x] == 1 and MAP[y + 1][x + 1] == 1:
                    rec_count += 1

print(rec_count)