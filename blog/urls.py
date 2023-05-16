from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("user/<str:username>/", UserPostListView.as_view(), name="user-posts"),
    path("about/", views.about, name="about"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),

]