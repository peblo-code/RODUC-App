from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

