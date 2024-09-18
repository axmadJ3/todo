from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Todo

def home(request):
    todos = Todo.objects.filter(is_done=False).all()
    return render(request, 'index.html', context={'todos': todos})


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