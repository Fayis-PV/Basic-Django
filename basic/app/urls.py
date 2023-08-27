from django.urls import path
from .views import *

# Create urls for App

app_name = 'app'
urlpatterns = [
    path('',index,name='home'),
    path('login',LoginView.as_view(),name='login'),
]
