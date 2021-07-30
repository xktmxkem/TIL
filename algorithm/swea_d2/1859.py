test = int(input())

for test in range(test):
    day = int(input())
    day_ls = list(map(int, input().split()))
    max_cost = max(day_ls)
    print(max_cost)