
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
MAP = [[0 for i in range(101)] for j in range(101)]
for i in info:
    x, y, d, g = i
    draw(x, y)

for i in MAP:
    print(i)