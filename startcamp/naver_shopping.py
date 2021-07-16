import requests
##json 파일을 이쁘게 보이게 하는 외부 모듈 
from pprint import pprint

query = '닌텐도'
url = f'https://openapi.naver.com/v1/search/shop.json?query={query}&sort=asc'

head = {
    'X-Naver-Client-Id': 'xfKs8JLwxTMrvnuoVjm1' ,
    'X-Naver-Client-Secret': 'dZIjuk7Vp9' 
}
##추가된 헤더정보 넣기
response = requests.get(url, headers=head).json()

#1. 반복문을 사용하여 각 제품마다 lprice를 출력
lprice = {}
for i in range(len(response['items'])):
    lprice[response['items'][i]['title']] = response['items'][i]['lprice']
#2. 가장 낮은값 출력
sorted(lprice.items(), key=lambda x: x[1])
msg = "검색하신 물품 최저가 상품 이름 : "+ list(lprice.keys())[0] +"가격 : " + list(lprice.values())[0]
print(msg)

##텔레그램
TOKEN = '1826034955:AAE-auv8OdnUwo_iqpJWDhb7FioCBD5Pigg'
url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1813255541&text={msg}."
response_telegram = requests.get(url_telegram).json()
