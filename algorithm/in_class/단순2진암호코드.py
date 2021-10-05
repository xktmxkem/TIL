

s = '01110110110001011101101100010110001000110100100110111011'  # 56 개
# 암호 비트 패턴이 7 자리 -> 총 8개가 나온다.
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
    '0001011': 9,
}
# 0111011(7) 0110001(5) 0111011(7) 0110001(5) 0110001(5) 0001101(0) 0010011(2) 0111011(7)
# [7,5,7,5,5,0,2,7] 이거 만들기
# 검증 확인하기

lst = []
for i in range(0, len(s), 7):
    key = s[i:i + 7]
    lst.append(pwd[key])

de = -1

sum = 0
for i in range(len(lst)):
    if (i + 1) % 2 == 0:
        sum += lst[i]
    else:
        sum += lst[i] * 3

# 올바른 검증 코드인지?
if sum % 10 == 0:
    print("올바르다")

else:
    print("안올바르다")