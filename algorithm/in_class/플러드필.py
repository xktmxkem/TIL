from collections import deque

def bfs(y, x, y1, x1):
    # 위 아래 왼쪽 오른쪽
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    queue = deque()
    queue.append([y, x])
    queue.append([y1, x1])
    lst[y][x] = 1
    lst[y1][x1] = 1

    while(len(queue) > 0):
        y, x = queue.popleft()
        ans = lst[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= 3 or nx >= 5:
                continue
            if lst[ny][nx] > 0:
                continue
            lst[ny][nx] = lst[y][x] + 1

            queue.append([ny, nx])

    return ans




is_max = 0
lst = [[0 for i in range(5)] for j in range(3)]
y, x, y1, x1= map(int, input().split())
ret = bfs(y, x, y1, x1)

for i in lst:
    print(i)
print('소요 일수 : {}'.format(ret))


## level까지 포함해서 저장하는 방법



#
# from collections import deque
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
#
# def bfs(sy, sx):
#     visited = [[0 for _ in range(5)] for _ in range(3)]
#     queue = deque()
#     queue.append((sy, sx, 1))
#     visited[sy][sx] = 1
#     ans = 0
#     while queue:
#         now = queue.popleft()  # [0]:y  [1]:x  // [2]: level
#         ans = now[2]
#         for t in range(4):
#             ny = now[0] + dy[t]
#             nx = now[1] + dx[t]
#             if ny < 0 or nx < 0 or ny >= 3 or nx >= 5: continue
#             if visited[ny][nx] == 1: continue
#             visited[ny][nx] = 1
#             queue.append((ny, nx, now[2] + 1))
#
#     return ans
#
#
# ret = bfs(0, 0)
# print(ret)