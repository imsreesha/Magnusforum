from django.shortcuts import render

# Create your views here
def askquestion(request):
    return render(request,'ask-question.html')