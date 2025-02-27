from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-cv/', views.create_cv, name='create_cv'),
    path('view-cv/', views.view_cv, name='view_cv'),
]
