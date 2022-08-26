import heapq
from collections import defaultdict
n = int(input())
m = int(input())
INF = float('inf')
distance = [[INF for i in range(n + 1)] for j in range(n + 1)]
info = defaultdict(set)

for i in range(m):
    s, e, c = map(int, input().split())
    if distance[s][e] > c:
        distance[s][e] = c
    info[s].add(e)


def find(start):
    global n
    distance[start][start] = 0
    q = [[0, start]]
    visited = [[0 for i in range(n + 1)] for j in range(n + 1)]
    visited[start][start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if distance[start][now] > cost:
            distance[start][now] = cost
        for next in info[now]:
            if visited[now][next]: continue
            visited[now][next] = 1
            heapq.heappush(q, [cost + distance[now][next], next])
for i in range(1, n + 1):
    find(i)

for i in range(1, n + 1):
    ans = [0 if i==INF else i for i in distance[i][1:]]
    print(' '.join(map(str, ans)))








