'''
 메모리: 60836 KB, 시간: 864 ms
 2022.04.29
 by Alub
'''
# N 현재 앱, M 확보해야할 바이트
N, M = map(int, input().split())
MEMORY = list(map(int, input().split()))
MEMORY.insert(0, 0)
COST = list(map(int, input().split()))
COST.insert(0, 0)
max_cost  = max(COST)
board = [[0 for i in range((max_cost * N) + 1)] for j in range(N+1)]
answer = 0
for i in range(1, N + 1):
    for j in range(1, (max_cost * N) + 1):
        memory = MEMORY[i]
        cost = COST[i]
        if j < cost:
            board[i][j] = board[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다
        else:
            board[i][j] = max(memory + board[i - 1][j - cost], board[i - 1][j])
        if board[i][j] >= M:
            answer = j
            break
print(answer)
