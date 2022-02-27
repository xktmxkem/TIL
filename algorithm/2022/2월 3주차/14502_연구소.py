import copy
from collections import deque

def combi(idx):
    if idx == len(VIRUS):
        temp = copy.deepcopy(TEST_CASE)
        VIRUS_CASE.append(temp)
        return
    TEST_CASE.append(VIRUS[idx])
    combi(idx + 1)
    TEST_CASE.pop()
    combi(idx + 1)

def infection(case):
    queue = deque(case)
    print(queue)



N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
# 0 빈 칸, 1 벽, 2 바이러스
# 2 <= 바이러스 <= 10
VIRUS = []
TEST_CASE = []
VIRUS_CASE = []
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 2:
            VIRUS.append([y, x])
combi(0)
for case in VIRUS_CASE:
    infection(case)
