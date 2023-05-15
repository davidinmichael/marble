from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
]