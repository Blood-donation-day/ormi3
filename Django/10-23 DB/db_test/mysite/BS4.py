import requests
import json
import sqlite3
from bs4 import BeautifulSoup


url = 'https://paullab.co.kr/bookservice/'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
data = []

name_list = []
price_list = []
author_list = []

# 책 이름
book_name = soup.select('.book_name')

for name in book_name:
    name_list.append(name.text)

# 가격 리스트 , 저자 리스트
book_info = soup.select('.book_detail>.book_info')
for i in range(0, len(book_info), 3):
    price_list.append(book_info[i].get_text()[4:])
for i in range(1, len(book_info), 3):
    author_list.append(book_info[i].get_text()[4:])

print(name_list)
print(price_list)
print(author_list)


# 데이터베이스에 연결
conn = sqlite3.connect('db.sqlite3')

# 커서 생성
cursor = conn.cursor()

# post 테이블 생성
cursor.execute(
    'CREATE TABLE book (id INTEGER, title TEXT, price TEXT, author TEXT)')

for i in range(len(name_list)):
    cursor.execute(
        f"INSERT INTO book VALUES ({i},'{name_list[i]}','{price_list[i]}', '{author_list[i]}')")

# output.json저장
conn.commit()
cursor.execute("SELECT * FROM book")
rows = cursor.fetchall()

output_data = [{"id": row[0], "title": row[1],
                "price": row[2], "author": row[3]} for row in rows]
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)


with open('output.json', 'r', encoding='utf-8') as f:
    json_content = json.load(f)
    print(json.dumps(json_content, ensure_ascii=False, indent=4))
conn.close()
