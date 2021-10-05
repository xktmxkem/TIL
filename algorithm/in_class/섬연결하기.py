min_cost = 1000000

def dfs(now, level, cost):
    global min_cost, n
    # 중간에 가격이 더 높다면 break
    if cost >= min_cost:
        return

    # 모든 곳을 다 돌았다면 break
    if level == n:
        min_cost = cost
        return

    for next in range(n):
        if MAP[now][next] > 0:



def solution(n, costs):
    answer = 0
    MAP = [[0 for i in range(n)] for j in range(n)]
    for i in costs:
        y, x, cost = i
        MAP[y][x] = cost
    print(MAP)


    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(n, costs)