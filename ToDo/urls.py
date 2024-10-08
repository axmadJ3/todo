from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-todo/', views.addTodo, name='add-todo'),
    path('completed/', views.completed_todos, name='completed-todos'),
    path('completed/<int:pk>', views.execute_completed, name='completed'),
    path('delete/<int:pk>', views.delete_todo, name='delete'),
]
