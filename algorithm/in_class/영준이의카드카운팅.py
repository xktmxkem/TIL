T = int(input())
for testcase in range(1 , T + 1):
    s = input()
    ans = ''
    card = {'S' : [i for i in range(1, 14)], 'D' : [i for i in range(1, 14)], 'H' : [i for i in range(1, 14)], 'C' : [i for i in range(1, 14)]}
    possible = 1
    for i in range(0, len(s), 3):
        temp = s[i:i + 3]
        card_num = 10 * int(temp[1]) + int(temp[2])
        try:
            card[temp[0]].remove(card_num)
        except:
            possible = 0
            break

    print('#{} '.format(testcase), end='')
    if possible:
        for i in card.values():
            print(len(i), end = ' ')
        print()
    else:
        print('ERROR')

