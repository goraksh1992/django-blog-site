from django.shortcuts import render, get_object_or_404
from .models import PostModel
from .forms import PostForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def blog_home(request):
    context = {
        "posts": PostModel.objects.all()
    }
    return render(request, 'blog/blog_home.html', context)


class PostListView(ListView):
    model = PostModel
    template_name = 'blog/blog_home.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'
    paginate_by = 3


class UserPostListView(ListView):
    model = PostModel
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostModel.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog/post-detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostModel
    fields = ['title', 'content']
    template_name = 'blog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostModel
    fields = ['title', 'content']
    template_name = 'blog/update_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostModel
    template_name = 'blog/delete_post.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





