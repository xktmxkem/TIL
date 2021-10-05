MAP = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}
s = '0F97A3'
new_s = ''

for i in range(len(s)):
    new_s += MAP[s[i]]

L = len(new_s) - len(new_s) % 7
for i in range(0, L, 7):
    print(int(new_s[i + i + 7], 2), end = ' ')

#[L] ~ [len(new_s) - 1]
#[L] ~ [len(new_s) - 1]
if L != len(new_s):
    print(int(new_s[L:len(new_s)],2))
# # 2 진수 - > 10진수로
# s = '1000111'
# sum = 0  # 10 진수를 계산
#
# for i in range(len(s)):
#     sum *= 2
#     sum += int(s[i])
#
# print(sum)