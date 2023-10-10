from django.shortcuts import render

db = [
    {
        'id' : 1,
        '글쓴이' : 'Soul',
        'created_at' : '2023-10-10 ',
        'title' : '제목',
        'contents' : '이글의 contents입니다.',
    },
    {
        'id' : 2,
        '글쓴이' : 'Soul2',
        'created_at' : '2023-10-10 ',
        'title' : 'title',
        'contents' : '이글의 contents입니다.',
    },
    {
        'id' : 3,
        '글쓴이' : 'Soul3',
        'created_at' : '2023-10-10 ',
        'title' : 'title',
        'contents' : '이글의 contents입니다.',
    },
]





def blog(request):
    context = {'db' : db}
    return render(request, 'blog/blog.html', context)
def post(request, posts):
    context = {'db' : db[posts-1]}
    return render(request, 'blog/post.html', context)

# Create your views here.
