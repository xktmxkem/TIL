class abc:
    def __init__(self, h, w):
        self.height = h
        self.weight = w


lst = [abc(180, 67), abc(170, 55), abc(180, 65), abc(180, 55), abc(165, 55), abc(170, 40)]
sort_lst = sorted(lst, key= lambda x : (-x.height, x.weight))

for i in sort_lst:
    print(i.height, i.weight, end='  #   ')