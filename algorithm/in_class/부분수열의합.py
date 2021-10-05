N, S = map(int, input().split())
lst = list(map(int , input().split()))

def dfs(idx, sum, flag) :
    global cnt
    if idx == N : # 0 1 2 3 ... N- 1 / 총 N개가 선택
       if sum == S and flag != 0 :
           cnt += 1
       return
    dfs(idx + 1, sum + lst[idx], 1) # 선택후 재귀호출
    dfs(idx + 1, sum , flag) # 안선택후 재귀호출

cnt = 0
dfs(0,0,0)
print(cnt)