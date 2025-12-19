# accounts/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import LoginView , ProfileView , RegisterView , LogoutView , ProfileUpdateView , UserDocumentView , MostanadatView


app_name = 'accounts'

urlpatterns = [
    path('',LoginView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    path('profile/',ProfileView.as_view(),name="profile"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('documents/', UserDocumentView.as_view(), name='documents'),
    path('total_mostandat/',MostanadatView.as_view(),name="total_mostandata"),
    
]
