from collections import deque

def dfs(now, s):
    global team_length
    global n
    if len(s) == team_length:
        team_combi.append(s)
        return


    for i in range(now + 1, n):
        dfs(i, s + str(i))

def str_dfs(now, a, combi):
    global max_sum
    if len(combi) == 2:
        max_sum += 
        return

    for i in range(now + 1, len(a)):
        str_dfs(i, a, combi + a[i])

# n은 무조건 짝수
# s.ij와 s.ji는 다를 수 도 있따.

n = int(input())
team_length = n // 2
team_combi = []
# board = [list(map(int, input().split())) for _ in range(n)]
s=''
dfs(-1, s)

max_sum = 0
i=0
while(i > (len(team_combi)//2)):
    combi = ''
    a_team = team_combi[i]
    b_team = team_combi[len(team_combi) - i]
    str_dfs(-1, a_team, combi)

