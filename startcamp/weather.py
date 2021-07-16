import requests
from requests.api import request
# 1132599

url = 'https://www.metaweather.com/api/location/1132599/2021/07/18'

response = requests.get(url).json()
print("서울의 모레 날씨는 " +response[0]['weather_state_name']+ "로 예상됩니다.")