import sys
input = sys.stdin.readline
edge = []
n, m = map(int, input().split())
for i in range(m):
    s, e, c= map(int, input().split())
    edge.append([s, e, c])
INF = float("inf")
distance = [INF for i in range(n + 1)]

def ford(start):
    global n, m
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            now = edge[j][0]
            next = edge[j][1]
            cost = edge[j][2]
            # 현재 간선을
            if distance[now] != INF and distance[next] > distance[now]:
                distance[next] = distance[now] + cost
                if i == n - 1:
                    return True
    return False

check = ford(1)
if check:
    print("-1")
else:
    for i in range(2, n + 1):
        if distance[i] ==  INF:
            print(-1)
        else:
            print(distance[i])