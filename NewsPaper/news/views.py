from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .filters import PostFilter
from .models import Post

class PostNList(ListView):
    model = Post
    template_name = 'news/posts_news.html'
    context_object_name = 'posts'
    ordering = ['-creation_date']
    filter_class = PostFilter
    paginate_by = 10

class PostNDetail(DetailView):
    model = Post
    template_name = 'news/post_news.html'
    context_object_name = 'post'

class Posts(View):
    def get(self, request):
        posts = Post.objects.order_by('-creation_date')
        paginator = Paginator(posts, 1)
        posts = paginator.get_page(request.GET.get('page', 1))
        data = {
            'posts': posts,
                }
        return render(request, 'news/posts_news.html', data)

class Search(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'search'
    ordering = ['-creation_date']
    filter_class = PostFilter
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=queryset)
        return self.filter.qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        return context