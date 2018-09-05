from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post

class PostList(ListView):
    paginate_by = 10
    def get_queryset(self):
        return Post.objects.filter(status='PUBLISHED')

class PostDetail(DetailView):
    model = Post

class PostListView(ListView):
    model = Post
    template_name = 'post/posts_list2.html'

class PostListByAuthor(ListView):
    paginate_by = 10
    template_name = 'post/posts_by_author.html'
    def get_queryset(self, **kwargs):
        return Post.objects.filter(author__username=self.kwargs['username'])

class PostListByYear(ListView):
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(publish__year=self.kwargs['year'])

class PostListByMonth(ListView):
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(publish__year=self.kwargs['year'], publish__month=self.kwargs['month'])

class PostListByDay(ListView):
    paginate_by = 10
    template_name = 'post/posts_by_author.html'
    def get_queryset(self, **kwargs):
        return Post.objects.filter(publish__year=self.kwargs['year'], publish__month=self.kwargs['month'], publish__day=self.kwargs['day'])
class PostAddView(CreateView):
    model = Post
    fields = ['title','subtitle','body','status']
    success_url = reverse_lazy('dj-admin-posts-view')
    template_name = 'post/posts_form.html'
    modo="create"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modo"] = self.modo
        return context

class PostEditView(UpdateView):
    model = Post
    modo="edit"
    fields = ['title','subtitle','body','status']
    success_url = reverse_lazy('dj-admin-posts-view')
    template_name = 'post/posts_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modo"] = self.modo
        return context