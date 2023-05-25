from django.urls import path, re_path
from . import views

urlpatterns = [
     re_path(r'^api/artisan/$', views.artisans_list),
     re_path(r'^api/artisan/([0-9]+)$', views.artisan_details),
     re_path(r'^api/artisandetail/([0-9]+)$', views.artisan_detail),

]