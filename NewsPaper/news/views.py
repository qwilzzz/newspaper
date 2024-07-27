from django.views.generic import ListView, DetailView
from .models import Post

class PostNList(ListView):
    model = Post
    template_name = 'news/posts_news.html'
    context_object_name = 'posts'


class PostNDetail(DetailView):
    model = Post
    template_name = 'news/post_news.html'
    context_object_name = 'post'
