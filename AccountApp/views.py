from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def userprofile(request):
    return render(request,'user-profile.html')
def userlist(request):
    return render(request,'user-list.html')
