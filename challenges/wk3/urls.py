from django.urls import path
from . import views

app_name = "wk3"
urlpatterns = [
    path("", views.index, name="index"),
    path("sussy", views.sussy, name="sussy"),
    path("bob", views.bob, name="bob")
]