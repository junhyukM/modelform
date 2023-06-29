from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('creates2/', views.create2, name='create2'),

    path('<int:id>/', views.detail, name='detail'),
]