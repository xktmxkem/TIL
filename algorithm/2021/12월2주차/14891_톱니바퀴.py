# 첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 상태는 8개의 정수로 이루어져 있고,
# 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.
#
# 다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다.
# 각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

# 2번 오른쪽 6번 왼쪽 0번 제일위
# SPIN = -1 : 왼쪽회전, 1 : 오른쪽회전 0 : 회전없음
def dfs(NUM, SPIN):
    global MID_1, MID_2, MID_3, MID_4
    if NUM < 0 or NUM > 3:
        return

    if VISITED[NUM] > 0 :
        return

    if SPIN == 1:
        if NUM == 1:
            MID_1 = MID_1  % 8
        elif NUM == 2:

        elif NUM == 3:

        elif NUM == 4:
    elif SPIN == -1:
        if NUM == 1:
            MID_1 =
        elif NUM == 2:

        elif NUM == 3:

        elif NUM == 4:
    else:
        if NUM == 1:
            MID_1 =
        elif NUM == 2:

        elif NUM == 3:

        elif NUM == 4:

GEAR1 = list(map(int, input().split()))
MID_1 = 0
GEAR2 = list(map(int, input().split()))
MID_2 = 0
GEAR3 = list(map(int, input().split()))
MID_3 = 0
GEAR4 = list(map(int, input().split()))
MID_4 = 0
K = int(input())
METHOD = []
for i in range(K):
    VISITED = [0, 0, 0, 0]
    NUM, SPIN = map(int, input().split())
    dfs(NUM, SPIN)

for j in