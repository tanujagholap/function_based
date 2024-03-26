from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *


@login_required(login_url='login_url')
def create_view(request):
    template_name = 'app1/create.html'
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def show_view(request):
    obj = Create.objects.all()
    template_name = 'app1/show.html'
    context = {'form': obj}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def update_view(request, pk):
    obj = Create.objects.get(id=pk)
    template_name = 'app1/create.html'
    form = CreateForm(instance=obj)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def delete_view(request, pk):
    template_name = 'app1/confirm.html'
    obj = Create.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, template_name)


