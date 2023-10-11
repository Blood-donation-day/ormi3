from django.shortcuts import render, redirect
from.models import Post
from django.db.models import Q

def blog(request):
    
    if request.GET.get('검색하기'):
        q = request.GET.get('검색하기')
        db = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q)).distinct()
    else:
        db = Post.objects.all().order_by('-pk')
    
    context = {
        'db' : db
    }
    return render(request, 'blog/blog.html', context)
def post(request, posts):
    db =Post.objects.get(pk=posts)
    if request.method == 'POST':
        d = Post.objects.get(pk=posts)
        d.delete()

        return redirect('/blog/')
    context = {
        'db' : db
    }
    return render(request, 'blog/post.html', context)
# Create your views here.


