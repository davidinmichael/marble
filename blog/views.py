from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = "posts"
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post-detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_form.html"
    fields = ['title', 'content', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    context = {
        "title" : "About",
    }
    return render(request, "blog/about.html", context)

