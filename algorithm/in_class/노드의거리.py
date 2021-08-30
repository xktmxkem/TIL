from collections import deque

def bfs(s):
    queue.append(s)
    visited[s] = 1


    while(queue):
        now = queue.popleft()
        if now == g:
            return visited[now] - 1
        for next in range(1, v + 1):
            if arg[now][next] == 0:
                continue
            if visited[next] > 0:
                continue
            visited[next] = visited[now] + 1
            queue.append(next)

    return 0



test = int(input())
for testcase in range(1, test + 1):
    v, e = map(int, input().split())
    arg = [[0 for i in range(v + 1)] for j in range(v + 1)]
    visited = [0 for i in range(v + 1)]

    queue = deque()

    for i in range(e):
        now, next = map(int, input().split())
        arg[now][next] = 1
        arg[next][now] = 1

    s, g = map(int, input().split())
    print('#{} {}'.format(testcase, bfs(s)))