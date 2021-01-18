from django.shortcuts import render
from .models import Blog
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.urls import reverse_lazy, reverse

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



