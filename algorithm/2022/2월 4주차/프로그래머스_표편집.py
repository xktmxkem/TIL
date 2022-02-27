from collections import deque
import heapq
import copy
# def solution(n, k, cmd):
#     answer = ''
#     lst = [i for i in range(n)]
#     original_lst = copy.deepcopy(lst)
#
#     removed = deque()
#     cursor = k
#     for word in cmd:
#         # 커서 위치 이동
#         if len(word) > 1:
#             a, b = word.split()
#             if a == 'D':
#                 cursor += int(b)
#             else:
#                 cursor -= int(b)
#         # 삭제 혹은 복구
#         else:
#             # 삭제
#             if word == 'C':
#                 # push pop 부분에서 n 만큼 시간 복잡도가 발생
#                 item = lst.pop(cursor)
#                 removed.append([cursor, item])
#                 # 만약 마지막 행인 경우 바로 윗행 선택
#                 if cursor == len(lst):
#                     cursor -= 1
#
#             # 복구
#             else:
#                 idx, num = removed.pop()
#                 lst.insert(idx, num)
#                 # 만약 현재 커서보다 작은 곳에서 복구 할 경우 현재커서 1 증가
#                 if idx <= cursor:
#                     cursor += 1
#
#
#     lst_idx = 0
#     for idx in range(n):
#         if lst_idx < len(lst):
#             if lst[lst_idx] == original_lst[idx]:
#                 answer += 'O'
#                 lst_idx += 1
#             else:
#                 answer += 'X'
#         else:
#             answer += "X"
#     return answer

def solution(n, k, cmd):
    answer = ''
    check = [['O'] * n]
    now = k
    max_heap = heapq.heapify([])
    min_heap = heapq.heapify([])
    for i in cmd:
        # 위치이동
        if len(i) > 1:
            a, b = i.split()
            # 아래로 내려감
            if a == 'U':
                print(a)
            # 위로 올라감:
            else:
                print(a)
        # 삭제 혹은 복구
        else:
            # 삭제
            if i == 'C':
                print(i)
            # 복그
            else:
                print(i)

    return answer


# "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
# # "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
# # "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# # "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
# n = 행(리스트)의 수
# k = 현재 위치
# cmd 들어올 명령의 수

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
solution(n, k, cmd)

# k = 5
# n = 6
# cmd = ['C', 'C', 'C', 'C', 'C', 'Z']
# solution(n, k, cmd)

# from heapq import heappush, heappop, heapify
#
# def solution(n, k, cmd):
#     maxh = [-x for x in range(k)]
#     minh = [x for x in range(k, n)]
#     heapify(maxh), heapify(minh)
#     removed = []
#     for command in cmd:
#         if command[0] == 'U':
#             for _ in range(int(command.split()[1])):
#                 heappush(minh, -heappop(maxh))
#         elif command[0] == 'D':
#             for _ in range(int(command.split()[1])):
#                 heappush(maxh, -heappop(minh))
#         elif command[0] == 'C':
#             removed.append(heappop(minh))
#             if not minh:
#                 minh.append(-heappop(maxh))
#         else:  # 'Z'
#             if removed[-1] > minh[0]:
#                 heappush(minh, removed.pop())
#             else:
#                 heappush(maxh, -removed.pop())
#
#     answer = ['O'] * n
#     for rem in removed:
#         answer[rem] = 'X'
#     return ''.join(answer)