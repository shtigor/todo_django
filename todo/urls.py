from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_list, name='todo_list'),
    path('update/', views.update_task, name='update_task'),
]
