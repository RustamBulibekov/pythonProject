from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post
from .permissions import MemberPermissionMixin


# Create your views here.


class PostListView(ListView):
    model = Post
    # template_name = 'blog/post_list.html'


class PostDetailListView(MemberPermissionMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail_post.html'
    # permission_required = 'blog.view_post'


class OwnLoginView(LoginView):
    template_name = 'accounts/login.html'
