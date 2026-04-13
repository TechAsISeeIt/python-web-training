from django.urls import path
from . import views

urlspatterns = [
    path("", views.core, name="core"),
    path("chat/", views.chat, name="chat"),
]
