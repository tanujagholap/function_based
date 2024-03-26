from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_view(request):
    template_name = 'app2/login.html'
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('show_url')
        else:
            return HttpResponse('plz enter correct username')
    return render(request, template_name)


@login_required(login_url='login_url')
def logout_view(request):
    logout(request)
    return redirect('signup_url')


def signup_view(request):
    template_name = 'app2/register.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registered successfully')
    context = {"form": form}
    return render(request, template_name, context)

