def func(level):
    global cnt
    if level == 5:
        print(subset)
        cnt += 1
        return

    subset.append(arr[level])
    func(level + 1) # 현재 level 원소 선택 O
    subset.pop()

    func(level + 1) # 현재 level 원소 선택 X


subset = []
arr = [1,3,5,7,9]

cnt = 0
func(0)