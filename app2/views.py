from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import LoginForm
# Create your views here.
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    
    data=Login(username=username, password=password)
    data.save()
    return render(request,'app2/index.html', {'lf':LoginForm})