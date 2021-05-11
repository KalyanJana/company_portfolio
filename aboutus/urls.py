from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_aboutus, name='all_aboutus'),
]
