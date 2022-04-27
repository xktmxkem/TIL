'''
 메모리: 30840 KB, 시간: 108 ms
 2022.04.28
 by Alub
'''
N = int(input())
time = [0 for i in range(N + 1)]
before = [[] for i in range(N + 1)]
dp = [0 for i in range(N + 1)]
#
def check(idx):
    if not dp[idx]:
        dp[idx] = time[idx] + max([check(i) for i in before[idx] if i !=[]], default=0)
    return dp[idx]

for i in range(1, N + 1):
    t, *b = map(int, input().split())
    time[i] = t
    before[i] = b[:-1]

for i in range(1, N + 1):
    print(check(i))