
T = int(input())

def dfs(idx) :
    if idx > N : return
    if tree[idx] > 0 : return
    dfs(idx * 2) # left subtree 값 채우기
    dfs(idx * 2 + 1) # right subtree 값 채우기

    # tree[idx]= tree[idx * 2 ] + tree[idx * 2 + 1]
    if idx * 2 <= N : tree[idx] += tree[idx * 2]
    if idx * 2 + 1 <= N : tree[idx] += tree[idx * 2 + 1]



for tc in range(1, T + 1) :
    N,M,L = map(int, input().split())
    tree = [0] * (N + 1)
    for i in range(M):
        a,b = map(int, input().split())
        tree[a] = b

    dfs(1)
    print("#{} {}".format(tc, tree[L]))