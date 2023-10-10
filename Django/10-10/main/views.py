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




def index(request):
    contents = {'db' : db}
    return render(request, 'main/index.html', contents)
def contact(request):
    return render(request, 'main/contact.html')
def about(request):
    return render(request, 'main/about.html')
# Create your views here.
