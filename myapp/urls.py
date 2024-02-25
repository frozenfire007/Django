from django.urls import path

from.views import home, root_page, temp_inherit_home, portfolio

urlpatterns = [
    path("home/", home),
    path("", root_page, name= "root_page"),
    path("temp-inherit-home/", temp_inherit_home, name="temp_inherit_home"),
    path("portfolio/", portfolio, name="portfolio")
]
