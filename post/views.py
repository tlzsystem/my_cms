from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    def get_queryset(self):
        return Post.objects.filter(status='PUBLISHED')

class PostDetail(DetailView):
    model = Post
