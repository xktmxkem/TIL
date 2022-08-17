import sys
input = sys.stdin.readline
# 이게 없으면 안돌아가짐
N = int(input())
T = list(map(int, input().split()))
Q = int(input())
DP = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    DP[i][i] = 1
for i in range(N-1):
    if T[i] == T[i + 1]: DP[i][i + 1] = 1

for i in range(2, N):
    for j in range(N - i):
        if T[j] == T[j + i] and DP[j + 1][i + j -1] == 1:
            DP[j][j+i] = 1


for i in range(Q):
    S, E = map(int, input().split())
    print(DP[S-1][E -1])

