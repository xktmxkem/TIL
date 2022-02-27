import heapq
#  n 로그 n
def solution(operations):
    min_heap = []
    max_heap = []
    for oper in operations:
        a, b = oper.split()
        if a == 'I':
            heapq.heappush(min_heap, int(b))
            heapq.heappush(max_heap, -int(b))
        else:
            # 최대값 삭제
            if b == '1':
                if len(max_heap) < 1:
                    continue
                temp = heapq.heappop(max_heap)
                min_heap.remove(-temp)
            # 최소값 삭제
            elif b == '-1':
                if len(min_heap) < 1:
                    continue
                temp = heapq.heappop(min_heap)
                max_heap.remove(-temp)

    if len(min_heap) < 1:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]


operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations))