from django.urls import path
from QuestionApp import views


urlpatterns = [
    path('',views.askquestion)
    
]