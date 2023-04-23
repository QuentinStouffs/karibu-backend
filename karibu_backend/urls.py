from django.urls import path, re_path
from . import views

urlpatterns = [
     path('home/', views.HomeView.as_view(), name ='home'),
     path('logout/', views.LogoutView.as_view(), name ='logout'),
     re_path(r'^api/users/$', views.users_list),
     re_path(r'^api/users/([0-9])$', views.users_detail),
]