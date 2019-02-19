from django.urls import path, re_path
from . import views

app_name='courses' 
urlpatterns = [
    path('', views.index , name='index'),
    path('details/<int:pk>/', views.details, name='details'),
]
