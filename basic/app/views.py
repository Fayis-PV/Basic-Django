from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from rest_framework.response import Response



# Create your views here.

def index(request):
    return render(request,'index.html')


class LoginView(APIView):
    form = AuthenticationForm
    
    def get(self,request):
        context = {
            'form':self.form
        }
        return render(request,'login.html',context)

    def post(self,request):
        form = self.form(request)
        if form.is_valid():
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return Response('Authenticated')
        else:
            return Response('Authentication Error')
        


class SignUpView(APIView):
    form = UserCreationForm

    def get(self,request):
        context = {
            'form':self.form
        }
        return render(request,'signup.html',context) 
    

