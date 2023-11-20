import requests

HOST = 'http://localhost:8000'
JOIN_URL = HOST + '/account/join/'
LOGIN_URL = HOST + '/account/login/'
LOGOUT_URL = HOST + '/account/logout/'
MYPAGE_URL = HOST + '/account/mypage/'
email = "test123@test123.com"
password = "chang123"

#회원가입
JOIN_FORM = {
"email": email,
"password1": password,
"password2": password
}
response = requests.post(JOIN_URL, JOIN_FORM)
print(response.json())

# 로그인
LOGIN_FORM = {
"email": email,
"password": password,
}

response = requests.post(LOGIN_URL, LOGIN_FORM)
print(f'access_token: {response.json()['access_token']}')
token = response.json()['access_token']


#로그아웃
response = requests.post(LOGOUT_URL)
print(response.json())


#Mypage
header = {
    'Authorization': 'Bearer ' + token
}

response = requests.get(MYPAGE_URL, headers=header)
print(response.json())

