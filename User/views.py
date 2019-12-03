from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from .models import Myuser
from .form import UserForm


@login_required
def user_list(request):
    users = Myuser.objects.all()
    return render(request, 'User/user_list.html', {'users':users})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return HttpResponseRedirect("/user/")
    else:
        form = UserForm()
        return render(request, 'User/user_edit.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(Myuser, pk=pk)
    user.delete()
    messages.success(request, "User successfully deleted!")
    return HttpResponseRedirect("/user/")


    #return render(request,'User/user_list.html', {'user':user})

def user_edit(request, pk):
    user = get_object_or_404(Myuser, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=True)
            return HttpResponseRedirect("/user/")
    else:
        form = UserForm(instance=user)
        return render(request, 'User/user_edit.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect("/user/")
    else:
        form = UserCreationForm()
    return render(request, 'User/signup.html', {'form': form})
