from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name='accounts/form.html',
    success_url=settings.LOGIN_URL,
)

login = LoginView.as_view(
    template_name='accounts/form.html',
)

logout = LogoutView.as_view(
    next_page='postlist'
)


@login_required
def profile(requset):
    return render(requset, 'accounts/profile.html')
# Create your views here.
