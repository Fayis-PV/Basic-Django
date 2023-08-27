from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from .forms import RegistrationForm
# from django.contrib.auth.views import LoginView 
from .forms import CustomAuthenticationForm
from allauth.account.views import SignupView,LoginView,LogoutView
from django.urls import reverse_lazy,reverse

# Create your views here.

def index(request):
    return render(request,'index.html')


class CustomAllAuthLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('home'))  # Redirect to home page if user is authenticated
        return super().get(request, *args, **kwargs)


class CustomSignUpView(SignupView):
    form = RegistrationForm

    def form_valid(self, form):
        # Create the user but don't log them in
        self.user = form.save(self.request)
        return redirect("account_login")  # Redirect to the login page

    # Optional: Override the success url to redirect after email confirmation
    def get_success_url(self):
        return reverse("account_login")  # Redirect to the login page
        
