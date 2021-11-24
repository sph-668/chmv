from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('search_date/', views.data_for_user, name='data_for_user'),
    path('search_more/', views.lessons_for_user, name='lessons_for_user'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', views.index_for_admin, name='index_for_admin'),


]