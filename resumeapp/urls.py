from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home' ),
    path('register', views.register, name= 'register'),
    path('signin/', views.signin, name = 'signin'),
    path('createresume/',  views.createresume, name = 'createresume'),
    path('cvtemplate/', views.cvtemplate, name= 'cvtemplate'),  
    path('logout', views.logout, name = 'logout'),
]