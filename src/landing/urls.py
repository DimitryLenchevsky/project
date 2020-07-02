from django.urls import path
from landing import views


app_name = 'landing'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('landing/', views.landing, name='landing'),
]