import base64



test = int(input())
for test in range(1, test + 1):
    str_encoding = input()
    str_bytes = base64.b64decode(str_encoding)
    str_decoding = str_bytes.decode('ascii')
    print(f'#{test} {str_decoding}')