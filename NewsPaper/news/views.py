from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .filters import PostFilter
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
class PostNList(ListView):
    model = Post
    template_name = 'news/posts_news.html'
    context_object_name = 'posts'
    ordering = ['-creation_date']
    filter_class = PostFilter
    paginate_by = 10
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)

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

class PostDetail(DetailView):
    template_name = 'news/post_detail.html'
    queryset = Post.objects.all()

class PostCreate(CreateView):
    template_name = 'news/post_create.html'
    form_class = PostForm

class PostUpdate(UpdateView):
    template_name = 'news/post_create.html'
    form_class = PostForm
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDelete(DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/../../'