from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')
def hi(request):
    return render(request,'hi.html')