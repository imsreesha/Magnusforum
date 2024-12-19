

from django.urls import path
from AccountApp import views


urlpatterns = [
    path('',views.login),
    path('k',views.hi),
    
]