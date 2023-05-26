from django.urls import path, re_path
from . import views

urlpatterns = [
     re_path(r'^api/artisan/$', views.artisans_list),
     re_path(r'^api/artisan/([0-9]+)$', views.artisan_details),
     re_path(r'^api/artisandetail/([0-9]+)$', views.artisan_detail),
     path("api/artisansearch/<str:lat>/<str:long>/<str:radius>/", views.get_artisans_by_radius),
     path("api/artisansearchbyaddress/<str:radius>/", views.get_artisans_by_address),
]