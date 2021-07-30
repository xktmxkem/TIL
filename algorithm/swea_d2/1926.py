n = range(1,int(input())+1)
n = list(map(str , n))

for i in n:
    result = 0
    result += i.count('3') + i.count('6') + i.count('9')
    if result == 0:
        print(i, end = ' ')
    else:
        print('-' * result,end = ' ')