from collections import deque


for i in range(1, 11):
    testcase = int(input())
    lst = list(map(int, input().split()))
    queue = deque()
    front = 0
    rear = 0
    for i in lst:
        queue.append(i)
        rear += 1

    while(1):
        ret = queue.popleft()
        front += 1
        if front > 5:
            front = 1
        ret = ret - front
        if ret < 1:
            ret = 0
            queue.append(ret)
            break
        queue.append(ret)

    result_s = '#{}'.format(testcase)
    for k in range(len(queue)):
        result_s += ' ' + str(queue.popleft())
    print(result_s)



