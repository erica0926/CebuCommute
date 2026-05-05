from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user, name='addUser'),
    path('userList/', views.user_list, name='userList'),
]
