'''
 메모리: 29200 KB, 시간: 308 ms
 2022.07.11
 by Alub
'''
# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

# 첫째 줄에 N이 주어진다. 둘째 줄부터 N2개의 줄에 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호가 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다.
#
# 학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생으로 이루어져 있다. 입력으로 주어지는 학생의 번호, 좋아하는 학생의 번호는 N2보다 작거나 같은 자연수이다.
# 어떤 학생이 자기 자신을 좋아하는 경우는 없다.

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 좋아하는 학생이 인접한 칸에 가장 많은 칸 자리
def check1(student, like_student):
    global N
    # 후보 리스트
    stack = [[-1, -1, -1]]
    for y in range(N):
        for x in range(N):
            if MAP[y][x] != 0: continue
            score = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    # 인접칸에 좋아하는 학생 있으면 후보 리스트에 넣음
                    if MAP[ny][nx] in like_student:
                        score += 1
            if score > stack[-1][2]:
                stack = [[y, x, score]]
            elif score == stack[-1][2]:
                stack.append([y, x, score])
    if len(stack) == 1:
        y = stack[0][0]
        x = stack[0][1]
        MAP[y][x] = student

    return stack

# 1을 만족하는 칸이 여러개이면 그 중 빈 칸이 가장 많은 칸으로 자리 정함
def check2(student, lst1):
    global N
    stack = [[-1, -1, -1]]
    for position in lst1:
        y = position[0]
        x = position[1]
        if MAP[y][x] != 0: continue
        score = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if MAP[ny][nx] == 0:
                    score += 1
        if score > stack[-1][2]:
            stack = [[y, x, score]]
        elif score == stack[-1][2]:
            stack.append([y, x, score])

    y = stack[0][0]
    x = stack[0][1]
    MAP[y][x] = student


# 2를 만족하는 칸도 여러개라면 행 번호 가장 작은것 그중에서도 열 번호가 가장 작은 칸으로
def check3():
    global N, LIKE_DICT, SCORE

    for y in range(N):
        for x in range(N):
            student = MAP[y][x]
            cnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if MAP[ny][nx] in LIKE_DICT[student]:
                        cnt += 1
            SCORE += int(10 ** (cnt - 1))

N = int(input())
LIKES = [list(map(int, input().split())) for _ in range(N ** 2)]
MAP = [[0 for i in range(N)] for j in range(N)]
LIKE_DICT = {}
SCORE = 0
for like in LIKES:
    student = like[0]
    like_student = like[1:]
    LIKE_DICT[student] = like_student
    lst1 = check1(student, like_student)
    if len(lst1) > 1:
        lst2 = check2(student, lst1)

check3()
print(SCORE)