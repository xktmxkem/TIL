import sys

sys.stdin = open("text.txt","r")

def insert_heap (val):
    tree.append(val)
    now = len(tree) - 1
    parent = now // 2
    # 자기자리 찾기
    while now > 1 and tree[parent] > tree[now]:
        # swap
        tree[parent], tree[now]  = tree[now], tree[parent]
        # now 를 갱신
        now = parent
        parent = now // 2




T = int (input())
for tc in range(1, T +1) :
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0]
    for val in lst :
        insert_heap(val)

    # 마지막 노드의 조상노드 전부 더하기 (조상노드 : root ~ 현재 노드까지의 경로상에 있는 모든 노드들)
    now = len(tree) - 1
    now //= 2
    parent = now // 2
    sum = 0
    while now != 0 :
        sum += tree[now]
        now //= 2
    print("#{} {}".format(tc, sum))