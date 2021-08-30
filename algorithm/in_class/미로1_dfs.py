

def dfs(y, x):
    global result
    # 범위 넘으면 return
    if y < 0 or x < 0 or y >= 16 or x >= 16:
        return 0

    # 벽이면 return
    if maze[y][x] == '1':
        return 0

    # 방문한 곳이면 return
    if visited[y][x] == '1':
        return 0
    # 방문지 초기화
    visited[y][x] = '1'

    # 도착시
    if maze[y][x] == '3':
        result = 1
        return 0

    # 상 하 좌 우
    dfs(y - 1, x)
    dfs(y + 1, x)
    dfs(y, x - 1)
    dfs(y, x + 1)

    return c





for test in range(1, 11):
    testcase = int(input())

    maze = [input() for i in range(16)]
    # dfs는 재귀라 함수내에 넣으면 계속 초기화됨
    result = 0
    visited = [[0 for i in range(16)] for j in range(16)]
    for y in range(16):
        for x in range(16):
            if maze[y][x] == '2':
               a = dfs(y, x)

    print('#{} {}'.format(testcase, result))
