from django.urls import path, re_path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
     path('home/', views.HomeView.as_view(), name ='home'),
     path('api/logout/', views.LogoutView.as_view(), name ='logout'),
     #Token management
    path('api/token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
    path('api/token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
     re_path(r'^api/users/$', views.users_list),
     path('api/users/<int:id>/', views.users_detail),
]