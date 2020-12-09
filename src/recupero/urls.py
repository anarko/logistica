from django.urls import path

from . import views

urlpatterns = [        
    path('', views.index, name='index'),
    path('upload_files_form/', views.upload_files_form , name='upload_files_form'),
    path('login/', views.login_user , name='login'),
    path('logout/', views.logout_user, name='logout'),
]