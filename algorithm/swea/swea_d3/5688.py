

def prime(num):
    board = [True for _ in range(num + 1)]

    root = int(num ** 0.5)
    for i in range(2, root):
        if board[i] == True:
           for j in range(i + i, num, i):
            board[j] = False

    temp = []
    for i in range(2, num):
        if board[i] == True:
            temp.append(i)
    temp.insert(0, 1)
    return temp


tc = int(input())
lst = prime(1000000)


for test in range(1, tc + 1):
    n = int(input())
    result_dict = {}
    if n == 1:
        print('#{} 1'.format(test))
    else:
        i = 1
        flag = True
        while ( n != 1):
            if n % lst[i] == 0:
                if lst[i] in result_dict.keys():
                    result_dict[lst[i]] += 1
                else:
                    result_dict[lst[i]] = 1
                n = n // lst[i]
            else:
                i += 1
                if i >= len(lst):
                    print('#{} -1'.format(test))
                    flag = False
                    break

        if flag:
            result = 1
            for key, value in result_dict.items():
                if value % 3 != 0:
                    print('#{} -1'.format(test))
                    break
                result *= key ** (value // 3)
            else:
                print('#{} {}'.format(test, result))
