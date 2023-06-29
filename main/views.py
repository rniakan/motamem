from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from users.models import Account

from django.shortcuts import render
from users.models import Post

class MainPageTemplateView(TemplateView):
    template_name = 'base/base_bootstrap.html'
    def get_context_data(self, **kwargs):
        kw = super(MainPageTemplateView, self).get_context_data(**kwargs)
        posts = Post.objects.all()
        posts_per_page = 1
        page = self.request.GET.get('page', 1)
        paginator = Paginator(posts, posts_per_page)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        page_numbers = list(paginator.page_range)
        kw.update({'page_numbers': page_numbers})
        kw.update({'posts': posts})
        print(page_numbers)
        return kw

# class PostDetailView(DetailView):
#     template_name = 'base/post_detail.html'
#     def get_context_data(self, **kwargs):
#         kw = super(PostDetailView, self).get_context_data(**kwargs)
#         posts = Post.objects.all()
#         kw.update({'posts': posts})
#         return kw

class PostDetailView(DetailView):
    model = Post
    template_name = 'base/post_detail.html'

