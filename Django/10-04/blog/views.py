from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.
db = {
        1 : {'title' : '제목1', 
            'contents' : 'Post 1 Body', 
            'img': 'https://cdn.discordapp.com/attachments/1000792779363995698/1147682470435749908/1692398735315.gif'
            },
        2 : {'title' : '제목2',
            'contents' : 'Post 2 Body',
            'img': 'https://cdn.discordapp.com/attachments/1000792779363995698/1147682470435749908/1692398735315.gif'
            },
        3 : {'title' : '제목33',
            'contents' : 'Post 3 Body',
            'img': 'https://cdn.discordapp.com/attachments/1000792779363995698/1147682470435749908/1692398735315.gif'
            },
    }
    
def blog(request):
    # db = Cafe.objects.all()를 하면 아래와 같이 값을 가져오게 됩니다.

    return render(request, 'blog/blog.html', {'db' : db})

def post(request, pk):
    # db = Cafe.objects.get(pk=pk)
    if db.get(pk):  # db에 pk(/1) 이 있으면 해당페이지
        return render(request, 'blog/post.html', {'post' : db.get(pk)})
    else:
        return HttpResponse('잘못된 접근입니다!')

def bookinfo(request):
    '''
    교육용 크롤링 페이지 입니다.
    '''
    url = 'https://paullab.co.kr/bookservice'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    result = []
    # print(soup.select('.book_name'))
    result = [f'<p>{i.text}</p>' for i in soup.select('.book_name')]
    return HttpResponse(result)