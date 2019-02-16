from django.urls import path
from . import views

app_name='core'                                                             # utilizado para viabilizar o namespace na versão 2.X
urlpatterns = [
    path('', views.home , name="home"),
    path('contato/', views.contact, name="contact"),
]
