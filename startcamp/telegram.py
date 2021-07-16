import requests
TOKEN = '1826034955:AAE-auv8OdnUwo_iqpJWDhb7FioCBD5Pigg'
msg = '메세지를 넣고 요청하면 텔레그램에 들어감'

##weather
#url_weather = 'https://www.metaweather.com/api/location/1132599/2021/07/18'

#response_weather = requests.get(url_weather).json()
#msg = "서울의 모레 날씨는 " +response_weather[0]['weather_state_name']+ "로 예상됩니다."

##미세먼지
service_key = 'stjlQoKqTsm4IBAGvPGwIa3rfwiC7FFtM9CkqUx7xxZInmSVJV09I8Fc9yPgArEEgkfnT%2BeSDxUg6uE6hp%2F7aA%3D%3D'
url_dust = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=강남구&dataTerm=month&pageNo=1&numOfRows=100&returnType=json&serviceKey={service_key}'
response_dust = requests.get(url_dust).json()
dust = response_dust['response']['body']['items'][0]["pm10Value"]

msg = (f"서울 강남구의 미세먼지 농도는 {dust}입니다.")


url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1813255541&text={msg}."
response_telegram = requests.get(url_telegram).json()
print(response_telegram)





