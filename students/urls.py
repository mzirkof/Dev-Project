from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('',views.students_list,name='list'),
    path('/<int:pk>',views.students_detail,name='detail')
]
