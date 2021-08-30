MAP = [
    [3,2,1,7],
    [1,2,3,4],
    [5,6,7,8],
    [1,1,1,1]
]

dr = [-1,-1,1,1]
dc = [-1,1,-1,1]

r,c = map(int,input().split())

max_val = int(-21e8)
max_point = (-1,-1)
for t in range(4) :
    nr = r + dr[t]
    nc = c + dc[t]
    if nr < 0 or nc < 0 or nr >= 4 or nc >= 4 : continue
    # max_val vs MAP[nr][nc]
    if max_val < MAP[nr][nc] :
        max_val = MAP[nr][nc]
        max_point = (nr,nc)

print("{} : {}".format(max_val , max_point))