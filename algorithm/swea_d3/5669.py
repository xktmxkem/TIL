# 세제곱수를 저장할 공간
num = [0]*(10**6+1)
 
# num[세제곱근]에 세제곱수를 저장
for q in range(1,10**6+1):
    num[q] = q**3
 
T = int(input())
 
for tc in range(1,1+T):
    n = int(input())
 
    # .index를 사용해서 n을 탐색할 때,
    # n이 num 안에 존재하지 않으면 오류 발생(n is not in list 오류)
    # 이를 해결하기 위해 예외처리로 문제 해결
    try:
        print('#{} {}'.format(tc,num.index(n)))
 
    except:
        print('#{} {}'.format(tc,-1))



# def prime(num):
#     num = int((num/2))
#     board = [True for _ in range(num + 1)]

#     root = int(num ** 0.5)
#     for i in range(1, root):
#         if board[i] == True:
#             if i != 1:
#                for j in range(i + i, num, i):
#                    board[j] = False

#     temp = []
#     for i in range(2, num):
#         if board[i] == True:
#             temp.append(i)

#     return temp


# lst = prime(1000000)

# tc = int(input())


# for test in range(1, tc + 1):
#     n = int(input())
#     result_dict = {}

#     i = 0

#     while ( n != 1):
#         if n % lst[i] == 0:
#             if lst[i] in result_dict:
#                 result_dict[lst[i]] += 1
#             else:
#                 result_dict[lst[i]] = 1
#             n = n // lst[i]
#         else:
#             i += 1

#     if len(result_dict) > 0:
#         for key, value in result_dict.items():
#             if value % 3 == 0:
#                 share = value // 3
#                 result = key * share
#                 print('#{} {}'.format(test, result))
#             else:
#                 print('#{} -1'.format(test))
#                 break
#     else:
#         print('#{} -1'.format(test))