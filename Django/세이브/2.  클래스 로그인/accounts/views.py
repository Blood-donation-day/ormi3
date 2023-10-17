from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# 이때까지 한건 FBV( Fuction Base view) 
# 이번에는 대부분 실무에 사용되는 CBV (Class Base View)


signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/form.html',
    success_url = settings.LOGIN_URL,
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

logout = LoginView.as_view(
    next_page = settings.LOGOUT_URL
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def logincheck(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/logincheck.html')
    return HttpResponse("로그인 안됨!")

def loginfbv(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('login 성공!')
        else:
            return HttpResponse('login 실패')

    return render(request, 'accounts/loginfbv.html')