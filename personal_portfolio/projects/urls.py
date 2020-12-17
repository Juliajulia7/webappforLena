from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("love_story/", views.love_story, name="love_story"),
    path("individual/", views.individual, name="individual"),
    path("family/", views.family, name="family"),
    path("about/", views.about, name="about"),
]