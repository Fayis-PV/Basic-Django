from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


# Create your views here.

def index(request):
    return render(request,'index.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


class SignUpView(APIView):
    form = RegistrationForm

    def get(self,request):
        context = {
            'form':self.form
        }
        return render(request,'signup.html',context) 
    

    def post(self,request):
        form = self.form(RegistrationForm)
        if form.is_valid():
            User.

