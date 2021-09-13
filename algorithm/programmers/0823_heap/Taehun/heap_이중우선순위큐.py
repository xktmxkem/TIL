import heapq


def solution(operations):
    max_heap = []
    min_heap = [] 
    for i in operations:
        order, number = i.split()
        number = int(number)
        if order == 'I':
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
    # 최대 삭제
        elif number == 1:
            if len(max_heap) < 1:
                continue
            a = heapq.heappop(max_heap)
            min_heap.remove(-a)
        else:
            if len(min_heap) < 1:
                continue
            a = heapq.heappop(min_heap)
            max_heap.remove(-a)

    if not min_heap:
        return [0,0]
    else:
        a = heapq.heappop(max_heap)
        b = heapq.heappop(min_heap)
        return [-a, b]


    return answer