from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.BlogCreate.as_view(), name='add-blog'),
    path('search/', views.BlogSearchView.as_view(), name = 'search-blog'),
    path('<int:pk>/', views.BlogDetail.as_view() , name = 'blog-detail'),
]