# postman이나 ThunderClient등 테스트 도구를 사용할 수 있다.

import requests

HOST = 'http://localhost:8000'
LOGIN_URL = HOST + '/account/login/'

# form에서 입력한 데이터 예시 
LOGIN_INFO = {
    "email": "chang@chang.com",
    "password": "soul4878"
}


# 로그인 요청
response = requests.post(LOGIN_URL, LOGIN_INFO)

print(response.text)
print(response.status_code)
print(response.json())
print('-------------------------------------')
print('access_token: ', response.json()['access_token'])


token = response.json()['access_token']

# 로그인한 사용자만 들어갈 수 있는 URL에 접속
# headers에 token을 넣어서 보냅니다.

header = {
    'Authorization': 'Bearer ' + token
}

data = {
    'title': '제목',
    'content': '제목',
    'author': 1,
}

res = requests.get(HOST + '/account/test/', headers=header, data=data)
print(res.status_code)
print(res.json())
