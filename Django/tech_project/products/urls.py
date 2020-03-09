from django.urls import path

from . import views

urlpatterns = [
    path('', views.admin_console, name='admin_console'),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirmdelete/', views.confirmed, name="confirmed"),
    path('createrecord/', views.createrecord, name="createrecord"),
]