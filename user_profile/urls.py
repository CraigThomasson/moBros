from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('sign-in/', views.sign_in, name='sign_in'),
]
