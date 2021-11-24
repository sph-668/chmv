from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('search_date/', views.data_for_user, name='data_for_user'),
    path('search_more/', views.lessons_for_user, name='lessons_for_user'),
    path('enter/', views.enter, name='enter'),
]