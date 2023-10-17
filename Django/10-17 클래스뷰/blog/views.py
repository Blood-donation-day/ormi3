from django.shortcuts import render
from .models import Post
from datetime import date 
def postlist(request):
    posts = Post.objects.all().order_by('-pk')
    # 연, 월 , 일과 일치하는 게시물 가져오기
    # posts = Post.objects.all().order_by('-pk').filter(created_at__year=2023)
    # posts = Post.objects.all().order_by('-pk').filter(created_at__month=2023)
    # posts = Post.objects.all().order_by('-pk').filter(created_at__day=2023)
    
    # 연, 월, 일에 매칭이 되는 게시물 가져오기
    # gt (greater than) : >
    # lt (less than) : <
    # gte (greater than or equal) : >=
    # lte (less than or equal) : <=
    # posts = Post.objects.all().order_by('-pk').filter(created_at__eq=date(2023, 10, 17))
    
    #     all()	테이블 모든 데이터 셋 가져오기
    # filter()	특정 조건에 부합하는 데이터셋 가져오기
    # exclude()	특정 조건을 제외한 데이터셋 가져오기
    # get()	특정 조건에 부합하는 1개의 데이터 가져오기
    # count()	가져올 데이터의 개수 가져오기
    # first()	첫번째 데이터 가져오기
    # last()	가장 마지막 데이터 가져오기
    # exists()	데이터 유무에 대한 결과(True, False)를 가져오기
    # order_by()	특정 필드 순서대로 정렬
    # 
    print(dir(request))
    print(request.user.password)
    print(request.GET.get('5', '5는 없다는데?'))
    print(request.POST)
    print(request.FILES)
    # 로그아웃 시 sessionid쿠키 사라짐 
    print(request.COOKIES)
    print(request.path)
    print(request.method)
    print(request.get_full_path_info)
    print(request.get_host())
    return render(request, 'blog/postlist.html', {'posts' : posts})

def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/postdetail.html', {'post':post})

def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'blog/postlist.html', {'posts':posts})

def posttest(request):
    posts = Post.objects.all().order_by('-pk').filter(created_at__gte=date(2023, 10, 17))
    return render(request, 'blog/posttest.html', {'posts' : posts})
# Create your views here.
