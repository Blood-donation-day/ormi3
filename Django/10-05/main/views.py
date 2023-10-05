from django.shortcuts import render
from django.http import HttpResponse

db = {
    1 : {'title' : '상품페이지1', 
            'contents' : 'Post 1 Body', 
            'img': 'https://cdn.discordapp.com/attachments/1000792779363995698/1147682470435749908/1692398735315.gif'
            },
        2 : {'title' : '상품페이지2',
            'contents' : 'Post 2 Body',
            'img': 'https://cdn.discordapp.com/attachments/1000792779363995698/1147682470435749908/1692398735315.gif'
            },
        3 : {'title' : '상품페이지3',
            'contents' : 'Post 3 Body',
            'img': 'https://cdn.discordapp.com/attachments/1000792779363995698/1147682470435749908/1692398735315.gif'
            },
}


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def product(request):
    return render(request, 'main/product.html')

def products(request, pk):
    if db.get(pk):
        return render(request, 'main/products.html', {'product' : db.get(pk)})
    return HttpResponse('잘못된 접근입니다!')

def contact(request):
    return render(request, 'main/contact.html')
def qna(request):
    return render(request, 'main/qna.html')
def qnas(request, qnas):
    return render(request, 'main/qnas.html', {'pages' : qnas})
# Create your views here.
