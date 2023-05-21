from django.urls import path , include 
from app2 import views


urlpatterns = [
    path('login/',views.login,name='login'),
]
