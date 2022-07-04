from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('signin', views.signin),

    path('', views.home),
    path('home', views.home),
    path('about', views.about),
    path('profile', views.profile),

    path('rookie', views.rookie),
    path('intermediate', views.intermediate),
    path('expert', views.expert),
]
