from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsDeleteView, NewsEditView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('add/', NewsCreateView.as_view(), name='news_add'),
    path('<int:pk>/edit/', NewsEditView.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

]
