from django.shortcuts import render
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
def home(request):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    return render(request,'home.html')

# User Register
def register(request):
    form=SignupForm
    if request.method=='POST':
        regForm=SignupForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered.')
    return render(request,'registration/register.html',{'form':form})
