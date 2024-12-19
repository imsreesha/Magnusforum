

from django.urls import path
from AccountApp import views


urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('userprofile/',views.userprofile),
    path('userlist/',views.userlist)
    
]