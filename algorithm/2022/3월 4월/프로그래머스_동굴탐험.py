# 모든 방을 적어도 한 번은 방문해야 합니다.
# 특정 방은 방문하기 전에 반드시 먼저 방문할 방이 정해져 있습니다.
# 2-1. 이는 A번 방은 방문하기 전에 반드시 B번 방을 먼저 방문해야 한다는 의미입니다.
# 2-2. 어떤 방을 방문하기 위해 반드시 먼저 방문해야 하는 방은 없거나 또는 1개 입니다.
# 2-3. 서로 다른 두 개 이상의 방에 대해 먼저 방문해야 하는 방이 같은 경우는 없습니다.
# # 2-4. 어떤 방이 먼저 방문해야 하는 방이면서 동시에 나중에 방문해야 되는 방인 경우는 없습니다.
# #
# # n은 2 이상 200,000 이하입니다.
# # path 배열의 세로(행) 길이는 n - 1 입니다.
# # path 배열의 원소는 [방 번호 A, 방 번호 B] 형태입니다.
# # 두 방 A, B사이를 연결하는 통로를 나타냅니다.
# # 통로가 연결하는 두 방 번호가 순서없이 들어있음에 주의하세요.
# # order 배열의 세로(행) 길이는 1 이상 (n / 2) 이하입니다.
# # order 배열의 원소는 [방 번호 A, 방 번호 B] 형태입니다.
# # A번 방을 먼저 방문한 후 B번 방을 방문해야 함을 나타냅니다.
from collections import defaultdict
def dfs(MAP, LIMIT)
def solution(n, path, order):
    answer = True
    MAP = defaultdict(list)
    LIMIT = defaultdict(int)
    LIMIT_CNT = len(order)
    for p in path:
        s, e = p
        MAP[s].append(e)
        MAP[e].append(s)
    for o in order:
        s, e = o
        LIMIT[s] = e

    print(MAP)
    return answer

solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]	)
===
from collections import deque
from collections import defaultdict
def dfs(n, MAP, LIMIT):
    queue = deque()
    queue.append(0)
    check = set()
    visited = [ 0 for i in range(n)]
    while queue:
        now = queue.popleft()
        check.add(now)
        if len(check) == n:
            return True
        for next in MAP[now]:
            if next in LIMIT.values():
                continue
            if visited[next]: continue
            visited[next] = 1

            if next in LIMIT.keys():
                queue.append(LIMIT[next])
                LIMIT[next] = -1
            queue.append(next)
    return False

def solution(n, path, order):
    answer = True
    MAP = defaultdict(list)
    LIMIT = {}
    for p in path:
        MAP[p[0]].append(p[1])
        MAP[p[1]].append(p[0])
    for o in order:
        s, e = o
        LIMIT[s] = e
    return dfs(n, MAP, LIMIT)