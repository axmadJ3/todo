from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('completed/', views.completed_todos, name='completed-todos'),
    path('completed/<int:pk>', views.execute_completed, name='completed'),
    path('delete/<int:pk>', views.delete_todo, name='delete'),
]
