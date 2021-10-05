def dfs(level):
    global max_num
    if level == N :
        #int(''.join(lst)) vs max_num
        max_num = max(int(''.join(lst)), max_num)
        return
    for y in range(len(lst)):
        for x in range(y + 1, len(lst)):
            lst[y], lst[x] = lst[x], lst[y]
            state = ''.join(lst) + "#" + str(level)
            if state in visited :
                lst[y],lst[x] = lst[x],lst[y]
                continue # 교환상태 + level 을 이용
            visited.add(state)
            dfs(level + 1)
            lst[y], lst[x] = lst[x], lst[y]

T = int(input())
for tc in range(1, T + 1) :
    lst , N = input().split()
    lst = list(lst)
    N = int(N)
    max_num = -int(21e8)
    visited = set()
    dfs(0)
    print("#{} {}".format(tc, max_num))