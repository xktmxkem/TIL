import sys
from collections import defaultdict
import heapq
import copy

input = sys.stdin.readline



v, e = map(int, input().split())
town = defaultdict(list)
cost = {}
answer = float("INF")
heap = []
dist = [[float("INF") for i in range(v + 1)] for j in range(v + 1)]
for i in range(e):
    s, e, c = map(int, input().split())
    town[s].append(e)
    cost[str(s)+str(e)] = c
    heapq.heappush(heap, [c, s, e])

while heap:
    c, s, g = heapq.heappop(heap)
    if s == g:
        answer = c
        break
    if c > dist[s][g]:
        continue

    for n_g in town[g]:
        n_c = c + cost[str(g) + str(n_g)]
        if n_c < dist[s][n_g]:
            dist[s][n_g] = n_c
            heapq.heappush(heap, [n_c, s, n_g])


print(-1 if answer == float("INF") else answer)

