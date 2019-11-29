from django.shortcuts import render, redirect
from .models import User
from .form import UserForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'User/user_list.html', {'products':users})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            product = form.save(commit=True)
            product.save()
            return redirect('User_list')
    else:
        form = UserForm()
        return render(request, 'User/user_edit.html', {'form': form})
