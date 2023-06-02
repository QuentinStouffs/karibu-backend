from django.urls import path, re_path
from . import views

urlpatterns = [
     re_path(r'^api/artisan/$', views.artisans_list),
     re_path(r'^api/artisan/([0-9]+)$', views.artisan_details),
     path('api/artisan/<int:id>/', views.artisan_details),
     path('api/artisanbyuser/<str:user>/', views.artisan_by_user),
     re_path(r'^api/artisandetail/([0-9]+)$', views.artisan_detail),
     path("api/artisansearch/<str:lat>/<str:long>/<str:radius>/", views.get_artisans_by_radius),
     path("api/artisansearchbyaddress/<str:radius>/", views.get_artisans_by_address),
     path("api/artisan/types/", views.types),
     path("api/geometry/", views.geo),
]