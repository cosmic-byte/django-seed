from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('list/', views.list, name='list'),
]
