
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('list/',views.ListUtilisation.as_view(),name="list utilisation"),

]
