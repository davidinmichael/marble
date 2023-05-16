from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import *

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 3
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user-post.html'
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Post Details"
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    context_object_name = "post"
    template_name = "blog/create-post.html"
    fields = ['title', 'content', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Create Post"
        return context

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    context_object_name = "post"
    template_name = "blog/update-post.html"
    fields = ["title", "content", "post_image"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            messages.warning(self.request, "You can't edit another User's Post")
            return redirect("home")
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Update Post"
        return context
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = "post"
    template_name = "blog/delete-post.html"
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            # messages.warning(request, "You can't edit another User's Post")
            # return redirect("home")
            return False

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Post Delete"
        return context

def about(request):
    context = {
        "title" : "About",
    }
    return render(request, "blog/about.html", context)

