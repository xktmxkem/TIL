import heapq
max_heap = []
min_heap = []
n = int(input())
for i in range(n):
    answer = 10001
    num = int(input())
    if max_heap:
        b_max = max_heap[0][1]
    else:
        b_max = 10001
    heapq.heappush(max_heap, [-num, num])

    if b_max != max_heap[0][1]:
        heapq.heappush(min_heap, max_heap[0][1])

    if len(min_heap) - len(max_heap) == 2:
        temp = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-temp, temp))

    elif len(max_heap) - len(min_heap) == 2:
        temp = heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, temp)


    print(max_heap[0][1])