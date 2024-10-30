from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import NewsForm, NewsFilterForm
from .mixins import UserIsOwnerMixin
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-published_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NewsFilterForm(self.request.GET)
        return context

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

class NewsCreateView(CreateView):
    model = News
    template_name = "news/news_form.html"
    form_class = NewsForm
    success_url = reverse_lazy("news_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class NewsPublishView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request, *args, **kwargs):
        news = self.get_object()
        news.status = "PU"
        news.save()
        return HttpResponseRedirect(reverse_lazy("news_list"))

    def get_object(self):
        news_id = self.kwargs.get("pk")
        return get_object_or_404(News, pk=news_id)

class NewsDeleteView(LoginRequiredMixin,UserIsOwnerMixin, DeleteView):
    model = News
    template_name = "news/news_confirm_delete.html"
    success_url = reverse_lazy('news_list')

class NewsEditView(UpdateView):
    model = News
    template_name = "news/news_form.html"
    form_class = NewsForm
    success_url = reverse_lazy('news_list')