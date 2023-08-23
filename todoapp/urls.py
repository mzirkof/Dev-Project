from django.urls import path
from . import views


urlpatterns = [
    path('todos',views.todo_list,name='todos'),
    path('todos/<int:pk>',views.todo_detail)
]
