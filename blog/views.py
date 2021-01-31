from django.shortcuts import render
from .models import Blog
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.urls import reverse_lazy, reverse
from django.db.models import Q, F

# Create your views here.

class BlogList(generic.ListView):
    template_name = 'blog/index.html'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(is_active=True)

class BlogDetail(generic.DetailView):
    model = Blog

class BlogCreate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Blog
    form_class = forms.BlogCreateForm
    template_name = 'blog/blog_form.html'
    success_message = 'Your blog is added successfully!!'

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('blog-list')

class BlogSearchView(generic.ListView):
    template_name = 'blog/blog_search.html'

    def get_queryset(self):
        object_list = Blog.objects.all()
        query = self.request.GET.get('q')
        if query:
            object_list = object_list.filter(Q(title__icontains=query) |
                                          Q(body__icontains=query) |
                                          Q(description__icontains=query),
                                          is_active=True)
        blog_type = self.request.GET.get('type')
        if blog_type:
            object_list = object_list.filter(Q(blog_type__name__icontains=blog_type))
        return object_list



