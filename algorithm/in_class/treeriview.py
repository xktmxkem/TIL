# from collections import deque

inorder = []
preorder = []
postorder = []

#
# def dfs(now, s):
#     print(s)
#     for next in range(9):
#         if arg[now][next] != 1:
#             continue
#         if visited[next] == 1:
#             continue
#         visited[next] = 1
#         dfs(next, s + str(next))
#
#
# def bfs(num):
#     queue = deque()
#     queue.append(num)
#     while (queue):
#         print(queue)
#         now = queue.popleft()
#         for next in range(9):
#             if arg[now][next] != 1:
#                 continue
#             if visited[next] == 1:
#                 continue
#             visited[next] = 1
#             queue.append(next)
#
#
# arg = [[0 for i in range(9)] for j in range(9)]
# visited = [0 for i in range(9)]
# arg[0][1] = 1
# arg[0][2] = 1
# arg[1][3] = 1
# arg[1][4] = 1
# arg[3][7] = 1
# arg[3][8] = 1
# arg[2][5] = 1
# arg[2][6] = 1
# s = '0'


# dfs(0, s)
# bfs(0)

# left, right 나눠서
# def dfstree(num):
#     if num == -1:
#         return
#     # 전위순회
#     preorder.append(num)
#     dfstree(left[num])
#     # 중위순회
#     inorder.append(num)
#     dfstree(right[num])
#     # 후위순회
#     postorder.append(num)
#
#
# # tree 복습 1
# left = [-1 for i in range(30)]
# right = [-1 for i in range(30)]
# left[0] = 1
# right[0] = 2
# left[1] = 3
# right[1] = 4
# left[3] = 7
# right[3] = 8
# left[2] = 5
# right[2] = 6
# inorder = []
# preorder = []
# postorder = []
# dfstree(0)
# print(f'전위 순회 {preorder}')
# print(f'중위 순회 {inorder}')
# print(f'후위 순회 {postorder}')

# tree 복습 인접리스트
# def neardfstree(num):
#
#     # 전위순회
#     preorder.append(num)
#     neardfstree(adj[num][0])
#     # 중위순회
#     inorder.append(num)
#     neardfstree(adj[num][1])
#     # 후위순회
#     postorder.append(num)
#
#
# adj = [[] for _ in range(9)]
# adj[0].append(1)
# adj[0].append(2)
# adj[1].append(3)
# adj[1].append(4)
# adj[2].append(5)
# adj[2].append(6)
# adj[3].append(7)
# adj[3].append(7)
# neardfstree(0)
# print(f'전위 순회 {preorder}')
# print(f'중위 순회 {inorder}')
# print(f'후위 순회 {postorder}')

# tree 복습 인덱스 리스트
# tree = ['#', 'a', 'b', 'c', 'd', 'e', '#', 'f', 'g', 'h']
# def idxdfs(idx):
#     # 인덱스 초과하면 에러
#     if idx >= len(tree):
#         return
#     # '#'이면 return
#     if tree[idx] == '#':
#         return
#     idxdfs(idx * 2) # 왼쪽자식
#     print(tree[idx], end = ' ')
#     idxdfs(idx * 2 + 1) # 오른쪽자식
#
#     return
#
# idxdfs(1)

