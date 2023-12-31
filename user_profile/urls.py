from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('register/', views.register_user, name='register_user'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('logout/', views.log_out, name='logout'),
]
