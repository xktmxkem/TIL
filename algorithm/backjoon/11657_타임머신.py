import heapq
from collections import defaultdict
n, m = map(int, input().split())
# . C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우
#만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.
town = defaultdict(set)
cost = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
for i in range(m):
    s, e, c = map(int, input().split())
    town[s].add(e)
    cost[s][e] = min(c, cost[s][e])


# cost, town
q = [[0, 1]]
distance = [float('inf') for i in range(n+1)]
loop = False
while q:
    c, now = heapq.heappop(q)
    if c >= distance[now]:
        continue
    if distance[now] != float('inf'):
        loop  = True
        break
    distance[now] = c
    for next in town[now]:
        n_c = c + cost[now][next]
        heapq.heappush(q, [n_c, next])
if loop:
    print(-1)
else:
    for i in range(2, len(distance)):
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])

