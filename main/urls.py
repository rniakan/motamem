
from django.contrib import admin
from django.urls import path, include
from .views import PostDetailView

from main.views import MainPageTemplateView
# from main.views import BasePostsTemplateView

urlpatterns = [
    path('', MainPageTemplateView.as_view(), name='main_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
