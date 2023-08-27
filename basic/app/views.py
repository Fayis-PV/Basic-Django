from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from .forms import RegistrationForm
# from django.contrib.auth.views import LoginView 
from .forms import CustomAuthenticationForm
from allauth.account.views import SignupView,LoginView
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index.html')


class CustomAllAuthLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'account/login.html'
    def get(self,request):
        if self.request.user.is_authenticated:
            return redirect('app:home')
        context ={
            'form':self.form_class
        }
        return render(request,'account/login.html',context)
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect('app:home')
        return super().form_valid(form)


class CustomSignUpView(SignupView):
    form = RegistrationForm

    def form_valid(self, form):
        # Create the user but don't log them in
        self.user = form.save(self.request)
        return redirect("account_login")  # Redirect to the login page

    # Optional: Override the success url to redirect after email confirmation
    def get_success_url(self):
        return reverse("account_login")  # Redirect to the login page
        
 

