from collections import deque

def bfs(y, x):

    queue = deque()
    # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited =  [[0 for i in range(16)] for j in range(16)]

    # 큐에 첫값 추가
    queue.append([y, x])

    while(len(queue) > 0):

        # now[0] = y
        # now[1] = x
        now = queue.popleft()

        for t in range(4):
            ny = now[0] + dy[t]
            nx = now[1] + dx[t]

            # 범위초과
            if ny < 0 or nx < 0 or ny >= 16 or nx >= 16:
                continue

            # 벽에 부딪힐때
            if maze[ny][nx] == '1':
                continue

            # 이미 방문했을때
            if visited[ny][nx] == 1:
                continue
            visited[ny][nx] = 1

            # 3이라면
            if maze[ny][nx] == '3':
                return 1

            # 다 아니라면 다음번 차례에 넘겨줌
            queue.append([ny, nx])


    return  0

for test in range(1, 11):
    testcase = int(input())

    maze = [input() for i in range(16)]

    for y in range(16):
        for x in range(16):
            if maze[y][x] == '2':
                result = bfs(y, x)

    print('#{} {}'.format(testcase, result))
