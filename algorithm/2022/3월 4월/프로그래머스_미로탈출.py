from collections import deque
from collections import defaultdict
import heapq
import copy


def solution(n, start, end, roads, traps):
    answer = 0
    road_info = defaultdict(lambda : defaultdict(list))
    check_trap = [1 for i in range(len(traps))]
    for road in roads:
        s, e, cost = road
        if s in traps or e in traps:
            road_info[e][s].append(-cost)
        road_info[s][e].append(cost)
    visited = [[] for i in range(1001)]

    queue = []
    for next in road_info[start]:
        for cost in road_info[start][next]:
            if cost < 0:continue
            heapq.heappush(queue, [cost , next, check_trap])
    while queue:
         now_cost, now, now_trap = heapq.heappop(queue)
         # 방문했다면 패스
         if now_trap in visited[now]: continue
         visited[now].append(now_trap)

         # 도착했다면 끝
         if now == end:
             answer = now_cost
             break

         # 지금 트랩에 왔다면 트랩 발동
         temp_trap = copy.deepcopy(now_trap)
         if now in traps:
             i = traps.index(now)
             temp_trap[i] *= -1

         for next in road_info[now]:
             for cost in road_info[now][next]:
                add_cost = cost
                # 둘다 함정
                if now in traps and next in traps:
                    trap1 = traps.index(now)
                    trap2 = traps.index(next)
                    add_cost *= temp_trap[trap1] * temp_trap[trap2]
                # 지금만 함정 다음껀 기본
                elif now in traps and next not in traps:
                    trap = traps.index(now)
                    add_cost *= temp_trap[trap]
                # 다음것이 함정
                elif now not in traps and next in traps:
                    trap = traps.index(next)
                    add_cost *= temp_trap[trap]
                if add_cost <= 0: continue
                heapq.heappush(queue, [now_cost + add_cost, next, temp_trap])
    return answer


#1
#solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
#2
#solution(5, 1, 5, [[1, 2, 1], [2, 3, 1], [3, 2, 1], [3, 5, 1], [1, 5, 10]], [2, 3])
#3
solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
