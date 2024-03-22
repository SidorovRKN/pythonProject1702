from django.http import HttpResponse
from django.shortcuts import render

from accounts.forms import LoginUserForm


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = LoginUserForm()

    return render(request, 'accounts/login.html', {'title': 'Авторизация', 'form': form})

def logout_user(request):
    return HttpResponse("logout")
