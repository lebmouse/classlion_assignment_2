from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Category, Tag
from .forms import PostForm
# Create your views here.


class PostLV(ListView):
    model = Post
    template_name = "pages/home.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostLV, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    # TODO:카테고리 완성하기
    def get_queryset(self, **kwargs):
        queryset = super(PostLV, self).get_queryset()
        try:
            category_id = self.kwargs['pk']
            queryset = queryset.filter(id=category_id)
        except:
            queryset = super(PostLV, self).get_queryset()
            
        return queryset
            


class PostDV(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'    
    success_url = reverse_lazy('post:home')
