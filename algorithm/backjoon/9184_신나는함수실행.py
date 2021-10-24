# def w(a, b, c):
#
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#
#     if a > 20 or b > 20 or c > 20:
#         w(20, 20, 20)
#
#
#
#     s1 = ''.join(map(str, [a-1, b-1, c]))
#     s2 = ''.join(map(str, [a - 1, b - 1, c]))
#     s3 = ''.join(map(str, [a - 1, b, c - 1]))
#     s4 = ''.join(map(str, [a - 1, b - 1, c - 1]))
#
#     if s1 in dic.values():
#         t1 = dic[s1]
#     else:
#         t1 = w(a-1, b, c)
#         dic[s1] = t1
#
#     if s2 in dic.values():
#         t2 = dic[s2]
#     else:
#         t2 = w(a-1, b-1, c)
#         dic[s2] = t2
#
#     if s3 in dic.values():
#         t3 = dic[s3]
#     else:
#         t3 = w(a-1, b, c-1)
#         dic[s1] = t3
#
#     if s4 in dic.values():
#         t4 = dic[s4]
#     else:
#         t4 = w(a-1, b-1, c-1)
#         dic[s4] = t4
#
#     if a < b < c:
#         return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
#
#     return t1 + t2 + t3 - t4
#
# dic = {}
# while(1):
#     x, y, z = map(int, input().split())
#
#     if x == -1 and y == -1 and z == -1:
#         break
#
#     print(f'w({x}, {y}, {z}) = {w(x, y, z)}')

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]


dp = [[[0 for i in range(20 + 1)] for j in range(20 + 1)] for k in range(20 + 1)]
while (1):
    x, y, z = map(int, input().split())

    if x == -1 and y == -1 and z == -1:
        break

    print(f'w({x}, {y}, {z}) = {w(x, y, z)}')

