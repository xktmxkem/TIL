def dfs(now_month, now_cost):
    global day, month, threemonth, year, min_cost
    # 기저조건
    if now_month > 12:
        return
    if now_cost >= min_cost:
        return


t = int(input())
for tc in range(1, t + 1):
    day, month, threemonth, year = map(int, input().split())
    plan = list(map(int, input().split()))
    min_cost = 10^8
    now_cost = 0
    print(plan)