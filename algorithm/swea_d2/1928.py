import base64

# def binary(num):
#     binary_list = []
#     while(1):
#         if num < 2 :
#             binary_list.append(1)
#             break
#         else:
#             binary_list.append(num%2)
#             num = int(num/2)
#     binary_list.reverse()
#     return(binary_list)


test = int(input())
for test in range(1, test + 1):
    str_encoding = input()
    str_bytes = base64.b64decode(str_encoding)
    str_decoding = str_bytes.decode('ascii')
    print(f'#{test} {str_decoding}')