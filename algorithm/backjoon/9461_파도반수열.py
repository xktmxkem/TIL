T = int(input())
lst = [1, 1, 1, 2, 2]
idx = 0
for i in range(4,200):
    lst.append(lst[i] + lst[idx])
    idx += 1

for tc in range(1, T + 1):
    N = int(input())
    print(lst[N - 1])