from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
# from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, HttpResponseForbidden
from main.models import POST
from django.db.models import Q


def blog(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        db = POST.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q)).distinct()
    else:
        db = POST.objects.all()
    context = {'db' : db,}
    
    return render(request, 'blog/blog.html', context)

def post(request, pk):
    db = POST.objects.get(pk=pk)
    context = {
        "db" : db,
    }
    return render(request, 'blog/post.html', context)

def test(request):
    data = [
        {'title' : 'Post1', 'text' : 'Text1', 'pk' : 1},
        {'title' : 'Post2', 'text' : 'Text2', 'pk' : 2},
        {'title' : 'Post3', 'text' : 'Text3', 'pk' : 3},
    ]
    s = '<h1>{{title}} </h1><p>{{text}}</p>'
    
    header = '<h2>hell world</h2>'
    main = render_to_string('blog/test.txt', {'data' : data[0]})
    footer = '<p>bye world</p>'
    
    
    #렌더가 하는 역할 그래서 css나 js를 못읽는 것입니다.
    # return HttpResponse(s.replace('{{title}}', data[0]['title']).replace('{{text}}', data[0]['text']))
    
    '''
    <p>hello blog</p>
    <p>{{ data.title }}</p>
    <p>{{ data.text }}</p>
    '''
    # return HttpResponse(header + main + footer)


    # DRF , REST API
    # fetch로 쇼핑몰 만들기와 같음.

    return JsonResponse(data, safe=False)

# Create your views here.
