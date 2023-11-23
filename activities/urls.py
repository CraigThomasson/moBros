from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activities'),  # domain/activities
    path('edit/<int:activity_id>/', views.edit_activity, name='edit_activity'),  # domain/activities/edit/1

]
