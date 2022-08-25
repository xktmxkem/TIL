n, m  = map(int, input().split())
town = []
for i in range(m):
    s, e, c = map(int ,input().split())
    town.append([s, e, c])
INF = float('inf')
distance = [INF for i in range(n + 1)]

def fold(start):
    global n, m
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            now, next, cost = town[j]

            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost
                if i == n -1:
                    return True
    return False

ans = fold(1)
if ans:
    print('-1')
else:
    for i in range(2, len(distance)):
            if distance[i] == INF:
                print('-1')
            else:
                print(distance[i])