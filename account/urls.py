from django.urls import path
from . import views

urlpatterns = [
    path("editprofile/", views.edit_profile, name='editprofile'),
    path("<str:username>/", views.user_profile, name="user_profile"),
]