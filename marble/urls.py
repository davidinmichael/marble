"""
URL configuration for marble project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account import views as account_views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("account/", include("account.urls")),
    path("register/", account_views.register, name="register"),
    path("login/", account_views.login_view, name="login"),
    # path("login/", auth_view.LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
]
