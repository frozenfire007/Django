from django.urls import path

from.views import home, root_page, temp_inherit_home

urlpatterns = [
    path("home/", home),
    path("", root_page),
    path("temp-inherit-home/", temp_inherit_home),
]
