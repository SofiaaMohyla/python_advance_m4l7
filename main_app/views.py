from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import NewsForm
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-published_at']

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

class NewsCreateView(CreateView):
    model = News
    template_name = "news/news_form.html"
    form_class = NewsForm
    success_url = reverse_lazy("news_list")

class NewsDeleteView(DeleteView):
    model = News
    template_name = "news/news_confirm_delete.html"
    success_url = reverse_lazy('news_list')

class NewsEditView(UpdateView):
    model = News
    template_name = "news/news_form.html"
    form_class = NewsForm
    success_url = reverse_lazy('news_list')