'''
 메모리: 118864 KB, 시간: 280 ms
 2022.05.02
 by Alub
'''
from collections import deque

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 동 - 서 - 남 - 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def rotate(x, d, k):
    q = deque()
    q.extend(graph[x])
    if d == 0:
        q.rotate(k)
    else:
        q.rotate(-k)
    graph[x] = list(q)


def change_avg():
    avg_count = 0
    all_sum = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                avg_count += 1
                all_sum += graph[i][j]
    if avg_count == 0:
        return False
    avg = all_sum / avg_count
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                if graph[i][j] > avg:
                    graph[i][j] -= 1
                elif graph[i][j] < avg:
                    graph[i][j] += 1
    return True

def solve(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    value = graph[x][y]
    graph[x][y] = 0
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > ny or ny >= m:
                if y == 0:
                    ny = m-1
                elif y == m-1:
                    ny = 0
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] == value:
                        count += 1
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        q.append((nx, ny))
    if count == 0:
        graph[x][y] = value
    return count


for _ in range(t):
    x, d, k = map(int, input().split())
    check_sum = 0
    for i in range(n):
        check_sum += sum(graph[i])
        if (i+1) % x == 0:
            rotate(i, d, k)
    if check_sum == 0:
        break
    else:
        visited = [[False] * m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and graph[i][j] != 0:
                    count += solve(i, j)
        if count == 0:
            change_avg()

answer = 0
for i in range(n):
    answer += sum(graph[i])

print(answer)