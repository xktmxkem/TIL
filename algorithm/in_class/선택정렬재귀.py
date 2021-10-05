def selectionsort(level):
    if level == len(lst):
        return

    min_value = 9999999999999999
    min_idx = -1
    for i in range(level, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_idx = i
    lst[level], lst[min_idx] = lst[min_idx], lst[min_idx]
    selectionsort(level + 1)

lst = [5,2,4,6,8,9,1]
selectionsort(0)
print(lst)