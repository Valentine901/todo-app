from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
# Create your views here.


def home(request):
    todo = Todo.objects.all()
    if request.method =='POST':
        forms = TodoForm(request.POST)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        forms = TodoForm()
    return render(request, 'home.html', {'forms':forms,'todos':todo} )



def delete_user(request, pk):
    delete_user = Todo.objects.get(id=pk)
    if request.method == 'POST':
        delete_user.delete()
        return redirect('home')
    else:
        return render(request, 'delete.html', {'delete_user':delete_user})


def update_user(request, pk):
    item = Todo.objects.get(id=pk)
    form = TodoForm(instance=item)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
            'forms':form,
        
        }
    return render(request, 'home.html', context)
    
