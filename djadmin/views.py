from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from post.models import Post

class Dashboard(TemplateView):
    template_name = 'djadmin/index.html';

class PostListView(ListView):
    model = Post
    template_name = 'djadmin/posts_list.html';

class PostAddView(CreateView):
    model = Post
    fields = ['title','subtitle','body','status']
    success_url = reverse_lazy('dj-admin-posts-view')
    template_name = 'djadmin/posts_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)