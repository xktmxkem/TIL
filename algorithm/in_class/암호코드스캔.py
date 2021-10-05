pwd = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

sixteen = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def make_sixcode(lst):
    temp_code = []
    for y in board:
        if len(set(y)) == 1:
            continue
        elif y in temp_code:
            continue
        else:
            temp_code.append(y)
    ans = []
    for i in temp_code:
        s = ''
        for j in i:
            if j != '0':
                s += j
            else:
                if len(s) != 0 and s not in ans:
                    ans.append(s)
                s = ''
    print(ans)
    return ans




t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    make_sixcode(board)




    # print(f'#{tc} {ten_code}')