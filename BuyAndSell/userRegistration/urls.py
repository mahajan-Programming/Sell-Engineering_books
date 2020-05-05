from django.urls import path

from . import views 
from userRegistration.views import index

urlpatterns = [
    path('', views.index, name='index'),
]