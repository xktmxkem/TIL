tree = {
    '030': ['054','002','045'],
    '054': ['001','009'],
    '002': [],
    '045': ['123'],
    '001': [],
    '123': [],
    '009': ['125','130'],
    '125': [],
    '130': []

}

def make_tree(node, level):
    if len(tree[node]) == 0 : # 리프노드일때
        print()
        return

    for child in tree[node]:
        if tree[node].index(child) != 0 : # 부모랑 바로 연결되지 않은경우
            for i in range(2*level+1):
                print("     ",end = '')

        if len(tree[node]) == 1: # 자식노드가 하나다
            print("---",end = '')

            #자식노드가 여러개
        elif tree[node].index(child) == len(tree[node]) - 1: # 마지막 자식노드
            print("--L", end = '')
        else:
            print("--+",end = '')

        print("--[" + child + "]",end =  '')
        make_tree(child,level + 1)

print('[030]',end ='')
make_tree('030', 0)