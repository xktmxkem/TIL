def enqueue(n):
    global rear
    global front
    lst[rear] = n
    rear += 1


def dequeue():
    global rear
    global front
    front += 1


test = int(input())
for testcase in range(1, test + 1):
    n, m = map(int, input().split())
    lst = [0 for _ in range(1030)]
    front = 0
    rear = 0

    input_lst = list(map(int, input().split()))

    for i in input_lst:
        enqueue(i)

    for j in range(m):
        enqueue(lst[front])
        dequeue()


    print('#{} {}'.format(testcase, lst[front]))


