from django.contrib import admin
from django.urls import path, include
from django.views import View
from demo_api.views import DemoApi

urlpatterns = [
    path('test/', DemoApi.as_view())
]
