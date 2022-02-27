# MST 최소신장트리
# 크루스칼 알고리즘  // 간선이 많은 경우
# 프림 알고리즘  // 간선이 적은 경우 

def union(a, b, parents):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parents[pb] = pa

def find(a, parents):
    if a == parents[a]:
        return a
    ret = find(parents[a], parents)
    parents[a] = ret
    return ret

def solution(n, costs):
    parents = [i for i in range(n)]
    costs = sorted(costs, key= lambda x : x[2])
    answer = 0
    for s, e, cost in costs:
        if find(s, parents) != find(e, parents):
            union(s, e, parents)
            answer += cost
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(n, costs)