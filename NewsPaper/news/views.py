from django.views.generic import ListView, DetailView
from .models import Post

class PostNList(ListView):
    model = Post
    template_name = 'news/posts_news.html'
    context_object_name = 'posts'
    ordering = ['-creation_date']


class PostNDetail(DetailView):
    model = Post
    template_name = 'news/post_news.html'
    context_object_name = 'post'
