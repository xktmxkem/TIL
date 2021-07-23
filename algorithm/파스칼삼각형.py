
n = int(input())
for i in range(n):

    a = int(input())
    temp_ls = []

    for i in range(1, a+1):
        if  i < 3:
            temp_ls.append(1)
            print(temp_ls)
        else:
            temp_ls.append(temp_ls[i-1] + (temp_ls[i-2]))
            temp_ls.insert(0, 1)
            temp_ls.insert(-1, 1)
    print(temp_ls)


