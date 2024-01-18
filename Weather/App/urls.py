from django.urls import path,include
from .views import *
from App import views
urlpatterns = [
    path('',views.index),
    path('city/',views.get)
    
]
