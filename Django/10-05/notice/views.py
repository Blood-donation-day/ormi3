from django.shortcuts import render

def notice(request):
    return render(request, 'notice.html')

def free(request):
    return render(request, 'free.html')
def frees(request, aa):
    return render(request, 'frees.html', {'pages' : aa})

def oneone(request):
    return render(request, 'oneone.html')

def oneones(request, ones):
    return render(request, 'oneones.html', {'pages' : ones})
# Create your views here.
