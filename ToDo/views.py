from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Todo
from .forms import AddForm

def home(request):
    todos = Todo.objects.filter(is_done=False).all()
    return render(request, 'index.html', context={'todos': todos})


def addTodo(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = AddForm()
    return render(request, 'ToDo/addTodo.html', context={'form': form})


def completed_todos(request):
    todos = Todo.objects.filter(is_done=True).all()
    return render(request, 'index.html', context={'todos': todos})


def execute_completed(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_done = True
    todo.save()
    return redirect('home')


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('home')