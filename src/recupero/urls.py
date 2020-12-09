from django.urls import path

from . import views

urlpatterns = [        
    path('', views.index, name='index'),
    path('menu1/', views.menu1 , name='menu1'),
    path('login/', views.login_user , name='login'),
    path('logout/', views.logout_user, name='logout'),
]