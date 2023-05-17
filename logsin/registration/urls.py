from django.urls import path
from . import views

urlpatterns=[
    path('signuppage',views.SignUp,name='signup'),
    path('',views.LoginPage,name='login'),
    #path('homepage',views.HomePage,name='home'),
    path('logoutpage',views.LogoutPage,name='logout'),
]