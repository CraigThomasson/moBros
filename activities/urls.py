from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activities'),  # domain/activities

]
